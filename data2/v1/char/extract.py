#!/usr/bin/env python
#
# > python --version
# Python 3.10.2
#
# A拼音 1.x 汉字频率数据提取
#
# 命令行格式:
# python extract.py core_freq.json DIR
import sys
import os
import io
import json
import sqlite3

# d_1.txt 文件头
文件头d1 = """\
# 注释: A拼音 1.x 汉字频率数据 (来源不清)
# 格式: 计数 汉字
"""

# 写一个输出文件
# 数据的格式: [(计数, 文本)]
def 写文件(文件名, 文件头, 数据):
    列表 = map(lambda x: str(x[0]) + " " + x[1], 数据)
    文本 = ("\n").join([文件头, ("\n").join(列表), ""])
    with io.open(文件名, "w", encoding="utf8") as f:
        f.write(文本)

# 生成 d_1.txt d_2.txt
def 生成d1d2(连接, 输出目录):
    # d_1.txt
    数据 = 连接.execute("SELECT 计数, 文本 FROM a WHERE 分级 IN ('a', 'b', 'c') ORDER BY 计数 DESC, 文本 ASC").fetchall()
    写文件(os.path.join(输出目录, "d_1.txt"), 文件头d1, 数据)
    # DEBUG
    print("d_1.txt = " + str(len(数据)))

    # d_2.txt
    数据 = 连接.execute("SELECT 计数, 文本 FROM a WHERE 分级 = 'd' AND 计数 > 2 ORDER BY 计数 DESC, 文本 ASC").fetchall()
    写文件(os.path.join(输出目录, "d_2.txt"), 文件头d1, 数据)
    # DEBUG
    print("d_2.txt = " + str(len(数据)))

def 构建数据库(连接, 数据):
    连接.execute("""
        CREATE TABLE a(
            文本 TEXT PRIMARY KEY,
            计数 INT NOT NULL DEFAULT 0,
            分级 TEXT)
    """)

    # 插入次数
    原始 = 数据["char_count"]["data"]
    插入 = [(汉字, 原始[汉字]) for 汉字 in 原始]

    连接.executemany("INSERT INTO a(文本, 计数) VALUES (?, ?)", 插入)

    # 插入分级
    原始 = 数据["pinyin_to_char"]
    更新 = []
    for i in 原始:
        for j in ["a", "b", "c", "d"]:
            if j in 原始[i]:
                for k in 原始[i][j]:
                    更新.append((j, k))
    连接.executemany("UPDATE a SET 分级 = ? WHERE 文本 = ?", 更新)

    # 统计
    测试 = 连接.execute("SELECT count(*) FROM a").fetchall()
    print("count(*) = " + str(测试[0][0]))

    测试 = 连接.execute("SELECT count(*) FROM a WHERE 分级 = 'a'").fetchall()
    print("count(*) a = " + str(测试[0][0]))

    测试 = 连接.execute("SELECT count(*) FROM a WHERE 分级 = 'b'").fetchall()
    print("count(*) b = " + str(测试[0][0]))

    测试 = 连接.execute("SELECT count(*) FROM a WHERE 分级 = 'c'").fetchall()
    print("count(*) c = " + str(测试[0][0]))

    测试 = 连接.execute("SELECT count(*) FROM a WHERE 分级 = 'd'").fetchall()
    print("count(*) d = " + str(测试[0][0]))

def main():
    # A拼音 1.x 原始数据 core_freq.json
    输入 = sys.argv[1]
    输出目录 = sys.argv[2]

    # 读取 json 文件
    with io.open(输入, "r", encoding="utf8") as f:
        输入文本 = f.read()
    数据 = json.loads(输入文本)

    # 构造数据库
    连接 = sqlite3.connect(":memory:")

    构建数据库(连接, 数据)

    生成d1d2(连接, 输出目录)

if __name__ == '__main__':
    main()
