# -*- coding: utf-8 -*-
# 词频统计：统计一段输入文本中每个单词出现的次数

import re
from collections import Counter


def main():
    # 读取用户输入的一段文本
    text = input("请输入一段文本：\n")

    # 去掉标点符号、统一转小写，再按空白切分成单词列表
    words = re.sub(r"[^\w\s]", "", text).lower().split()

    # 用 Counter 统计词频，并按出现次数从高到低打印
    for word, count in Counter(words).most_common():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
