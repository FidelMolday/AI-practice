from chatterbot import ChatBot
from chatterbot.trainer import ChatterBotCorpusTrainer

bot = ChatBot("My Bot")

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.curpus.english.greetings",
              "chatterbot.curpus.english.conversations")

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    response = bot.get_response(user_input)
    print("Bot ", response)