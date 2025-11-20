from flask import Flask
import threading
import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Telegram actif !"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # On lance le bot dans un thread
    threading.Thread(target=run_bot).start()

    # Lancer le serveur web (Render nécessite un port ouvert)
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
