import os
import re
from pathlib import Path

INPUT_DIR = Path("inputs")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)
INPUT_DIR.mkdir(exist_ok=True)

def read_text_file(file_path: Path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        返回f。读取()

def 分割句子(文本: 字符串):
    text = re.sub(r'\s+', ' ', text.strip())
    sentences = re.split(r'(?<=[。！？.!?])\s*', text)
    返回[s.去除空格()对于s在句子中如果]

def summarize_text(text: str, max_sentences: int = 5) -> str:
    """
    简单摘要：按句子长度和关键词频率挑选最重要句子。
    """
句子 =拆分句子(文本)
    如果len(句子)<= 最大句子数：
        返回 " ".join(f"-{s}" forsinsentences)

    keywords = [
        "重要", "结论", "方法", "步骤", "总结", "注意", "关键", "核心",
        "学习", "练习", "考试", "作业", "任务", "目标", "实现", "提高"
    ]

    scored = []
    对于索引idx，句子sent在 枚举(句子):
        score = 0
        for kw in keywords:
            if kw in sent:
                score += 2
        score += min(len(sent) / 20, 5)
        scored.append((score, idx, sent))

    scored.sort(reverse=True)
    selected = sorted(scored[:max_sentences], key=lambda x: x[1])
    返回 " ".join(f"-{s}" for_, _, sinselected)

def generate_todo_list(text: str):
所有 =[]
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    对于行在行：
        如果任何(k在行中包含[“作业”,“考试”“复习”“练习”“实验”“提交”“完成”]):
todos.append(行)

    如果 不是所有：
所有 =[
            "整理学习内容并复习重点",
            "完成相关练习题",
            "检查是否有作业或实验需要提交"
        ]
    返回前8个[:8]

 generate_report(input_name: str, text: str) -> str:
摘要 =summarize_text(文本)
待办事项 =generate_todo_list(文本)

报告 =f"""# 学习资料处理报告

## 输入文件
- 文件名：{input_name}

## 自动摘要
{摘要}

## 待办清单
"""
    for i, todo in enumerate(todos, 1):
        report += f"{i}. {todo}\n"

    report += """
## 说明
本报告由本地学习助手自动生成，用于帮助整理学习材料、提炼重点并生成行动清单。
"""
    返回report

 主函数():
    print("=== AI 学习助手 ===")
    files = list(INPUT_DIR.glob("*.txt")) + list(INPUT_DIR.glob("*.md"))

    如果 没有文件：
        print("inputs/ 目录下没有找到 txt 或 md 文件。")
        print("请先放入一个示例文件，例如 inputs/sample.txt")
        return

    print("检测到以下输入文件：")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f.name}")

    for file_path in files:
        print(f"\n正在处理：{file_path.name}")
        text = read_text_file(file_path)
报告 =生成报告(文件路径.名称, 文本)

输出文件 = 输出目录 /f"{文件路径.主干}_摘要.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"已生成：{output_file}")

如果__name__ =="__main__":
    main()
