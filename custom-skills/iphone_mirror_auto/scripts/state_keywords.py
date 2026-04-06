"""Keyword-to-state mapping for the traffic study automation state machine.

Each state defines:
  - keywords: text patterns to detect this state (any match triggers)
  - action: what to do when this state is detected
  - target: the text to click (if action is "click")
  - next_state: expected state after action (for verification)
"""

from enum import Enum, auto


class State(Enum):
    UNKNOWN = auto()
    APP_HOME = auto()           # 交警12123 main page
    MY_BUSINESS = auto()        # 我的业务 tab
    IN_PROGRESS = auto()        # 办理中 list
    STUDY_REDUCE = auto()       # 学法减分 detail page
    READY_TO_STUDY = auto()     # 准备学习 page
    VIDEO_LIST = auto()         # Video list page
    VIDEO_PLAYING = auto()      # Video playback
    VIDEO_ENDED = auto()        # Video completion dialog
    FACE_RECOGNITION = auto()   # Face recognition popup
    EXAM_READY = auto()         # Ready to start exam
    EXAM_QUESTION = auto()      # Answering a question
    EXAM_SUBMIT = auto()        # Ready to submit exam
    EXAM_RESULT = auto()        # Exam result page
    STUDY_COMPLETE = auto()     # All done
    ERROR = auto()              # Error state


# Keywords that indicate each state.
# Order matters: more specific states should be checked first.
STATE_KEYWORDS = [
    {
        "state": State.FACE_RECOGNITION,
        "keywords": ["人脸识别", "人脸认证", "身份验证", "请正对摄像头", "面部识别"],
        "action": "wait",  # handled by independent face_monitor.py; main loop just waits
        "description": "Face recognition popup",
    },
    {
        "state": State.VIDEO_ENDED,
        "keywords": ["视频播放完毕", "已完成观看", "本次学习结束"],
        "action": "click",
        "target": "确定",
        "description": "Video ended dialog",
    },
    {
        "state": State.STUDY_COMPLETE,
        "keywords": ["累积学时已满", "完成学习要求", "已符合", "本课件已完成学习"],
        "action": "submit_study",
        "target": "提交",
        "description": "Study time reached 30 min, submit learning record",
    },
    {
        "state": State.EXAM_RESULT,
        "keywords": ["考试结果", "考试通过", "考试未通过", "恭喜", "及格", "不及格"],
        "action": "report_result",
        "description": "Exam result page",
    },
    {
        "state": State.EXAM_QUESTION,
        "keywords": ["下一题"],
        "action": "wait",  # exam answering handled by auto_exam.py + Claude; main loop just waits
        "description": "Exam question page",
    },
    {
        "state": State.EXAM_READY,
        "keywords": ["开始考试"],
        "action": "click",
        "target": "开始考试",
        "description": "Ready to start exam",
    },
    {
        "state": State.VIDEO_PLAYING,
        "keywords": ["结束学习"],
        "action": "monitor_video",
        "description": "Video is playing",
    },
    {
        "state": State.VIDEO_LIST,
        "keywords": ["选择视频", "视频列表", "请选择", "推荐视频", "视频学习"],
        "action": "select_video",
        "description": "Video selection list",
    },
    {
        "state": State.READY_TO_STUDY,
        "keywords": ["开始学习"],
        "action": "click",
        "target": "开始学习",
        "description": "Ready to start studying",
    },
    {
        "state": State.STUDY_REDUCE,
        "keywords": ["去学习"],
        "action": "click",
        "target": "去学习",
        "description": "Study reduce detail page",
    },
    {
        "state": State.IN_PROGRESS,
        "keywords": ["学法减分"],
        "action": "click",
        "target": "学法减分",
        "description": "In-progress business list",
    },
    {
        "state": State.MY_BUSINESS,
        "keywords": ["办理中"],
        "action": "click",
        "target": "办理中",
        "description": "My business tab",
    },
    {
        "state": State.APP_HOME,
        "keywords": ["我的业务", "首页"],
        "action": "click",
        "target": "我的业务",
        "description": "App home page",
    },
]


def detect_state(ocr_results):
    """Detect the current state based on OCR results.

    Checks keywords in priority order (most specific first).

    Args:
        ocr_results: List of OCR result dicts from ocr_engine.

    Returns:
        Tuple of (State, state_config_dict) or (State.UNKNOWN, None).
    """
    all_text = " ".join(r["text"] for r in ocr_results)

    for state_config in STATE_KEYWORDS:
        for keyword in state_config["keywords"]:
            if keyword in all_text:
                return state_config["state"], state_config
    return State.UNKNOWN, None
