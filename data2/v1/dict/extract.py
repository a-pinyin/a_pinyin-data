#!/usr/bin/env python
#
# > python --version
# Python 3.10.2
#
# A拼音 1.x 内置词典数据提取
#
# 命令行格式:
# python extract.py core_data.db DIR
import sys
import os
import io
import sqlite3

# d_1.txt 文件头
文件头d1 = """\
# 注释: A拼音 1.x 内置词典数据 (来源不清)
# 格式: 计数 词
"""

# symbol2.txt 文件头
文件头s2 = """\
# 注释: A拼音 1.x 中文标点数据 (来源不清)
# 格式: 计数 文本
"""

# 写一个输出文件
# 数据的格式: [(计数, 文本)]
def 写文件(文件名, 文件头, 数据):
    列表 = map(lambda x: str(x[0]) + " " + x[1], 数据)
    文本 = ("\n").join([文件头, ("\n").join(列表), ""])
    with io.open(文件名, "w", encoding="utf8") as f:
        f.write(文本)

# 生成 d_1.txt d_2.txt 等
def 生成d1等(连接, 输出目录):
    数据 = 连接.execute("SELECT count, word FROM a_pinyin_core_dict ORDER BY count DESC, word ASC").fetchall()
    # 每一万行一个文件
    行数 = 1_0000
    for i in range(0, len(数据), 行数):
        部分 = 数据[i:i + 行数]
        序号 = int(i / 行数) + 1
        写文件("d_" + str(序号) + ".txt", 文件头d1, 部分)

# 生成 symbol2.txt
def 生成s2(连接, 输出目录):
    数据 = 连接.execute("SELECT count, text FROM a_pinyin_symbol2 ORDER BY count DESC, text ASC").fetchall()
    写文件(os.path.join(输出目录, "symbol2.txt"), 文件头s2, 数据)

def main():
    # A拼音 1.x 内置数据库 core_data.db
    数据库 = sys.argv[1]
    输出目录 = sys.argv[2]

    # 打开数据库
    连接 = sqlite3.connect(数据库)

    生成d1等(连接, 输出目录)
    生成s2(连接, 输出目录)

if __name__ == '__main__':
    main()
