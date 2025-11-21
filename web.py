import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Token
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# 🖼️ PHOTO
PHOTO_START_URL = "https://image2url.com/images/1763587287262-54768308-b40a-4f85-93fd-32ddce56375e.jpeg"


# -----------------------------
#         COMMANDE /START
# -----------------------------
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton("Informations ℹ️", callback_data="info"),
        InlineKeyboardButton("Contact 📱", callback_data="contact")
    )

    keyboard.add(
        InlineKeyboardButton("Mini-App 🎮", url="https://grosbagel93-cell.github.io/La-stuperie74/")
    )

    keyboard.add(
        InlineKeyboardButton("Telegram 📺", url="https://google.com"),
        InlineKeyboardButton("Snapchat 👻", url="https://google.com")
    )

    keyboard.add(
        InlineKeyboardButton("Potato 🥔", url="https://google.com"),
        InlineKeyboardButton("Instagram 📸", url="https://google.com")
    )

    keyboard.add(
        InlineKeyboardButton("Linkbio 🔗", url="https://google.com")
    )

    bot.send_photo(
        message.chat.id,
        PHOTO_START_URL,
        caption="BONJOUR À TOUS 👋\n\nBienvenue sur notre BOT Officiel 🤖\n\nClique sur « Mini-App » pour accéder au menu 🎮📍",
        reply_markup=keyboard
    )


# -----------------------------
#          CALLBACKS
# -----------------------------
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.data == "info":
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="ℹ️ Informations :\n\nTu peux modifier ce texte."
        )

    elif call.data == "contact":
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption="📞 Contact :\n\nMets ton contact ici."
        )


# -----------------------------
#        LANCEMENT
# -----------------------------
from flask import Flask, request
import telebot
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(
        request.stream.read().decode("utf-8")
    )
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
