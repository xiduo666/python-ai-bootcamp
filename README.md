# python-ai-bootcamp

7 天 Python 前置课练习记录（AI 开发方向）。
最终目标：独立调用 Kimi API，写出带上下文记忆的多轮对话命令行程序。

## 目录

- `day01/` 课表查询 1.0：字典 + while 循环输入（见 python-learning 仓库或本地）
- `day02/` 课表查询 2.0：文件读写 + JSON 闭环（`class_schedule.py` + `schedule.json`）

## Day 1–2 已掌握

- 字典：`.get()` 安全取值、增删改查
- 字符串：`strip()`、`split()`、`in`
- 文件：`with open()` 读写，`r/w` 模式区别（踩过 `io.UnsupportedOperation: not writable`）
- JSON：`json.dumps()` / `json.loads()` 互转，走通 文件 → 字符串 → 字典 → 修改 → 写回 闭环
- 报错阅读：JSONDecodeError、ValueError 拆包失败

## 遗留问题（后续课程解决）

1. **文件不存在时会崩**：`schedule.json` 被删掉后程序启动直接 `FileNotFoundError`。
   → Day 5 学 try/except 后处理：文件不存在则创建默认课表。
2. **JSON 内容格式坏了会崩**：用户手改 json 文件改出语法错误，`json.loads()` 抛 JSONDecodeError。
   → 同样归 Day 5 异常处理。
3. **Windows 绝对路径写死**：`C:\Users\...` 换台电脑就废。
   → 已改为相对路径，约定 json 与脚本同目录；Day 5 结合环境变量进一步规范。
4. **修改模式没有单条撤销**：输错一对键值只能重新改回来，没有 undo。
   → 属于进阶需求，结课后可自行扩展。
5. **查询/修改全靠精确匹配**：用户输"星期三"而非"周三"就查不到。
   → 可在输入侧做别名映射，属优化项。
