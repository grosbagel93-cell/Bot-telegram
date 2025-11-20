import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask

# Bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Flask server (obligatoire pour Render)
app = Flask(__name__)

# Route simple pour Render
@app.route("/")
def home():
    return "Bot Telegram OK"

# Photo d'accueil
PHOTO_START_URL = "https://image2url.com/images/1763587287262-54768308-b40a-4f85-93fd-32ddce56375e.jpeg"

# Commande /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("Informations ℹ️", callback_data="info"),
        InlineKeyboardButton("Contact 📱", callback_data="contact")
    )

    markup.add(
        InlineKeyboardButton("Mini-App 🎮", url="https://grosbagel93-cell.github.io/La-stuperie74/")
    )

    markup.add(
        InlineKeyboardButton("Telegram 📺", url="https://google.com"),
        InlineKeyboardButton("Snapchat 👻", url="https://google.com")
    )

    markup.add(
        InlineKeyboardButton("Potato 🥔", url="https://google.com"),
        InlineKeyboardButton("Instagram 📸", url="https://google.com")
    )

    markup.add(
        InlineKeyboardButton("Linkbio 🔗", url="https://google.com")
    )

    bot.send_photo(
        message.chat.id,
        PHOTO_START_URL,
        caption="BONJOUR 👋\nBienvenue sur le bot officiel 🎮📍",
        reply_markup=markup
    )

# Boutons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "info":
        bot.edit_message_caption(
            "ℹ️ Informations",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
    elif call.data == "contact":
        bot.edit_message_caption(
            "📞 Contact",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )

# Lancement bot + Flask
if __name__ == "__main__":
    # Lancer le polling dans un thread
    import threading
    threading.Thread(target=lambda: bot.infinity_polling()).start()

    # Lancer Flask pour Render (port dynamique)
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
