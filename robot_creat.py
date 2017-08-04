# coding:utf-8
"""
初始创建聊天机器人
"""
from chatterbot import ChatBot


chatbot = ChatBot(
    name='Umer',

    storage_adapter='chatterbot.storage.SQLStorageAdapter',

    database='./database.sqlite3',

    logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch'
    },
    {
        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
        'threshold': 0.55,
        'default_response': '抱歉，这个问题暂时无法回答你'
    }
]
)
