# coding:utf-8
"""
训练模块
"""
import sys
import robot_creat
from chatterbot.trainers import ChatterBotCorpusTrainer


def robot_train(data):
    print("训练开始\n请耐心等待...")
    robot = robot_creat.chatbot
    robot.set_trainer(ChatterBotCorpusTrainer)
    robot.train(data)
    print("训练结束")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        corpus = sys.argv[1:]
        robot_train(corpus)
    else:
        print(sys.argv)
        print("""请输入训练的语料库.
Try 'python robot_train.py corpus1 corpus2 ...'
""")
