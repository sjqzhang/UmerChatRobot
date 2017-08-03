# coding:utf-8

from chatterbot import ChatBot


# 创建一个聊天机器人
chatbot = ChatBot(
    name='Umer',
    #storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            'default_response': '抱歉，这个问题暂时无法回答你'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'

)

conversation = [
"你好",
"你好，请问有什么能帮你",
"互联网医疗哪家强",
"优麦",
"谢谢夸奖",
"不用谢"
]

chatbot.train(conversation)

# Get a response to the input text '
print("你好，请问有什么能帮你")
while True:
    question = input(">>>")
    answer = chatbot.get_response(question)
    print(answer)
chatbot.trainer.export_for_training('./my_export.json')