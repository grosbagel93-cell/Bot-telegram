import telebot
from flask import Flask, request

API_TOKEN = "8587383482:AAHnoeBYhluich_l00TCiIGfkn10MgSBYR8"   # ← mets le nouveau token ici
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# START
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 Bot en ligne ! Envoie-moi un message.")

# MESSAGE TEXTE
@bot.message_handler(func=lambda m: True)
def text_handler(message):
    bot.reply_to(message, f"Tu as dit : {message.text}")

# WEBHOOK (obligatoire pour Render)
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
