# coding:utf-8

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# 创建一个聊天机器人
chatbot = ChatBot(
    name='Umer',

    read_only=True,  # 是否进行学习

    storage_adapter='chatterbot.storage.SQLStorageAdapter',

    database='./database.sqlite3',

    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            'default_response': '抱歉，这个问题暂时无法回答你'
        }
    ]
)

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.udf")

# Get a response to the input text '
print("你好，请问有什么能帮你")
while True:
    question = input(">>>")
    answer = chatbot.get_response(question)
    print(answer)
