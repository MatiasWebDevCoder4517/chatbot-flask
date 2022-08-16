from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("api/chatbot/data/data.yml")


@app.route("/")
def index():
    # to send context to html
    return render_template("api/chatbot/templates/index.html")


@app.route("/get")
def get_bot_response():
    # get data from input,we write js  to index.html
    userText = request.args.get("msg")
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
