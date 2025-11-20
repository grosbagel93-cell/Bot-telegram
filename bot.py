import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 Récupération du token depuis Render
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialisation du bot
bot = telebot.TeleBot(BOT_TOKEN)

# 🖼️ PHOTO D’ACCUEIL
PHOTO_START_URL = "https://image2url.com/images/1763587287262-54768308-b40a-4f85-93fd-32ddce56375e.jpeg"


# -----------------------------
#         COMMANDE /START
# -----------------------------
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()

    # Ligne 1
    keyboard.add(
        InlineKeyboardButton("Informations ℹ️", callback_data="info"),
        InlineKeyboardButton("Contact 📱", callback_data="contact")
    )

    # Ligne 2 — Mini-App
    keyboard.add(
        InlineKeyboardButton("Mini-App 🎮", url="https://grosbagel93-cell.github.io/La-stuperie74/")
    )

    # Ligne 3
    keyboard.add(
        InlineKeyboardButton("Telegram 📺", url="https://google.com"),
        InlineKeyboardButton("Snapchat 👻", url="https://google.com")
    )

    # Ligne 4
    keyboard.add(
        InlineKeyboardButton("Potato 🥔", url="https://google.com"),
        InlineKeyboardButton("Instagram 📸", url="https://google.com")
    )

    # Ligne 5
    keyboard.add(
        InlineKeyboardButton("Linkbio 🔗", url="https://google.com")
    )

    bot.send_photo(
        message.chat.id,
        PHOTO_START_URL,
        caption=(
            "BONJOUR À TOUS 👋\n\n"
            "Bienvenue sur notre BOT Officiel 🤖\n\n"
            "Clique sur « Mini-App » pour accéder au menu 🎮📍"
        ),
        reply_markup=keyboard
    )


# -----------------------------
#             CALLBACKS
# -----------------------------
@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    if call.data == "info":
        bot.edit_message_caption(
            caption="ℹ️ Informations :\n\nTu peux modifier ce texte.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )

    elif call.data == "contact":
        bot.edit_message_caption(
            caption="📞 Contact :\n\nMets ton contact ici.",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )


# -----------------------------
#         LANCEMENT BOT
# -----------------------------
if __name__ == "__main__":
    bot.infinity_polling()
