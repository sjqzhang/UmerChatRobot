# coding:utf-8
"""
浏览聊天机器人语料库默认读取路径下的所有语料库
"""
import os
from corpus_path import find_dst
from functools import cmp_to_key


def browse_folder():

    def compare(x, y):
        stat_x = os.stat(dst + "/" + x)
        stat_y = os.stat(dst + "/" + y)
        if stat_x.st_ctime > stat_y.st_ctime:
            return -1
        elif stat_x.st_ctime < stat_y.st_ctime:
            return 1
        else:
            return 0

    dst = find_dst()
    corpus = os.listdir(dst)
    key = cmp_to_key(compare)
    corpus = sorted(corpus, key=key)
    print("所有语料库如下(按添加时间由新到旧排序)：")
    for folder in corpus:
        print(folder)

if __name__ == '__main__':
    browse_folder()
