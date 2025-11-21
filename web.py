import telebot
from flask import Flask, request

API_TOKEN = "8587383482:AAHnoeBYhluich_l00TCiIGfkn10MgSBYR8"
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Route GET pour éviter l’erreur 405
@app.route('/', methods=['GET'])
def index():
    return "Bot is running", 200

# Webhook pour recevoir les updates de Telegram
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
