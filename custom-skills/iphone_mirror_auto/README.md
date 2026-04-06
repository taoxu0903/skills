# Traffic Study Automation (交警12123 学法减分)

通过 macOS iPhone Mirroring 自动化交警12123 app 的"学法减分"流程。

## 功能

| 模式 | 触发方式 | 说明 |
|------|----------|------|
| **视频学习** | `/traffic-study 学法减分` | 自动导航、选视频、播放、累计30分钟后提交 |
| **手动答题** | `/traffic-study 答题` | 截屏识别题目，Claude 告诉你答案，你自己点击 |
| **自动答题** | `/traffic-study 自动答题` | 截屏识别题目，Claude 分析后自动点击答案和下一题 |

人脸识别弹框由独立的后台监测进程处理，1秒轮询，检测到立刻发 macOS 通知。

## 环境要求

- macOS Sequoia+ (需要 iPhone Mirroring 功能)
- iPhone Mirroring 窗口打开且**不能缩放**（必须保持原始大小）
- iPhone 必须**锁屏**状态（解锁后镜像会断开）
- [Claude Code](https://claude.ai/claude-code) 安装并配置好 skill
- `cliclick`：`brew install cliclick`
- Python 依赖：`pyobjc-framework-Vision`、`pyobjc-framework-Quartz`、`Pillow`

## 目录结构

```
iphone_mirror_auto/
├── SKILL.md                 # Claude Code skill 定义
├── README.md                # 本文件
├── scripts/                 # 所有可执行脚本
│   ├── face_monitor.py      # 人脸识别后台监测 (1s轮询)
│   ├── auto_exam.py         # 自动答题: capture + click 子命令
│   ├── exam_helper.py       # 手动答题: 截屏+OCR提取题目
│   ├── traffic_study.py     # 视频学习: 状态机主循环
│   ├── ocr_engine.py        # Apple Vision OCR (快速模式)
│   ├── screen_utils.py      # 截屏 + 窗口检测
│   ├── input_utils.py       # 鼠标点击 + 坐标转换
│   └── state_keywords.py    # 状态关键词映射
└── references/              # 参考文档
    ├── technical-notes.md   # 技术实现细节
    ├── claude-loop-vs-natural-loop.md
    └── 交警12123-学法减分自动化方案.md
```

## 工作原理

### 截屏 → OCR → 决策 → 点击

```
iPhone Mirroring 窗口
       │
       ▼ screencapture -x -o -l <windowID>
    截屏 PNG
       │
       ▼ Apple Vision OCR (level 0 快速模式)
    文字 + 边界框坐标
       │
       ▼ 关键词匹配 / Claude LLM 分析
    决策：点哪里
       │
       ▼ cliclick c:X,Y
    点击 → iPhone 触摸事件
```

### 三种执行模式的区别

| | 视频学习 | 手动答题 | 自动答题 |
|---|---|---|---|
| **决策者** | Python 脚本 (规则匹配) | Claude (LLM推理) | Claude (LLM推理) |
| **循环方式** | Python `while True` | 用户手动触发每题 | Claude 自然循环 |
| **点击执行** | Python 脚本自动点 | 用户手动点 | Python 脚本自动点 |
| **Claude 参与** | 只启动，不参与循环 | 每题分析一次 | 每题分析+指挥点击 |

### 人脸识别监测

独立后台进程 `face_monitor.py`，与主流程完全解耦：

```
face_monitor.py (后台)          主流程 (视频/答题)
    │                               │
    ├─ 每1秒截屏+OCR               ├─ 正常执行任务
    ├─ 检测到人脸弹框?              ├─ 遇到未知状态?
    │  YES → macOS通知             │  → 等待重试
    │  NO  → 继续轮询              │  → 继续轮询
    └─ 弹框消失? → 通知"已通过"      └─ 自动恢复
```

## 使用方法

所有操作通过 Claude Code 的 `/traffic-study` skill 触发：

```bash
# 1. 视频学习 (自动看视频30分钟)
/traffic-study 学法减分

# 2. 手动答题 (每题手动触发)
/traffic-study 答题

# 3. 自动答题 (20题自动完成)
/traffic-study 自动答题
```

## Skill 安装

确保 `~/.claude/skills/traffic-study/skill.md` 软链接指向本项目的 `SKILL.md`：

```bash
mkdir -p ~/.claude/skills/traffic-study
ln -s /path/to/iphone_mirror_auto/SKILL.md ~/.claude/skills/traffic-study/skill.md
```
