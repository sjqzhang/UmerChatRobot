# coding:utf-8
"""
删除一些语料库
"""
import sys
import os
import shutil
from corpus_path import find_dst

def delete_corpus(*target):
    """
    param target: 需要删除的语料库(接收零个或多个值作为参数)
    """
    dst = find_dst()
    all_corpus = os.listdir(dst)

    target = target[0]
    for each in target:
        if each in all_corpus:
            shutil.rmtree(dst + each)
        else:
            print(each + ",此语料库不存在")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        #print('[Y/N]')
        #if
        delete_obj = sys.argv[1:]
        delete_corpus(delete_obj)
    else:
        print("""请指定需要删除的语料库
Try 'python corpus_remove.py target1 target2 ...'        
""")