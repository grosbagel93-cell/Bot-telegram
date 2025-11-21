import telebot
from flask import Flask, request

# ------------ TOKEN ------------
API_TOKEN = "8587383482:AAHnoeBYhluich_l00TCiIGfkn10MgSBYR8"
bot = telebot.TeleBot(API_TOKEN)

# ------------ FLASK APP ------------
app = Flask(__name__)

# ------------ HANDLER START ------------
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    # Ligne 1
    keyboard.add(
        telebot.types.InlineKeyboardButton("Informations ℹ️", callback_data="info"),
        telebot.types.InlineKeyboardButton("Contact 📱", callback_data="contact")
    )

    # Ligne 2 — Mini-App
    keyboard.add(
        telebot.types.InlineKeyboardButton("Mini-App 🎮", url="https://grosbagel93-cell.github.io/La-stuperie74/")
    )

    # Ligne 3
    keyboard.add(
        telebot.types.InlineKeyboardButton("Telegram 📺", url="https://google.com"),
        telebot.types.InlineKeyboardButton("Snapchat 👻", url="https://google.com")
    )

    # Ligne 4
    keyboard.add(
        telebot.types.InlineKeyboardButton("Potato 🥔", url="https://google.com"),
        telebot.types.InlineKeyboardButton("Instagram 📸", url="https://google.com")
    )

    # Ligne 5
    keyboard.add(
        telebot.types.InlineKeyboardButton("Linkbio 🔗", url="https://google.com")
    )

    bot.send_photo(
        message.chat.id,
        "https://image2url.com/images/1763587287262-54768308-b40a-4f85-93fd-32ddce56375e.jpeg",
        caption=(
            "BONJOUR À TOUS 👋\n\n"
            "Bienvenue sur notre BOT Officiel 🤖\n\n"
            "Clique sur « Mini-App » pour accéder au menu 🎮📍"
        ),
        reply_markup=keyboard
    )

# ------------ WEBHOOK ------------
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.stream.read().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# ------------ RUN SERVER ------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
