# coding:utf-8
"""
将自定义的语料库添加到聊天机器人默认读取路径
"""
import sys
from corpus_path import find_dst
import shutil


def move_folder(src):
    """
    param src: 自定义语料库文件夹的读取路径
    return: None
    """
    dst = find_dst()
    shutil.move(src, dst)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        from_folder = sys.argv[1]
        move_folder(from_folder)
    else:
        print("""请指定自定义的语料库文件夹的读取路径。
Try 'python corpus_install.py from_folder'
""")
