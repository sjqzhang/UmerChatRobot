# coding:utf-8
"""
寻找chatter_corpus模块的安装路径
"""
import chatterbot_corpus

def find_dst():
    dst = ''.join(chatterbot_corpus.__path__) + '/data/'
    return dst