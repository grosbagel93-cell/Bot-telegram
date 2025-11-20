import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# 🔑 Render va récupérer ton token automatiquement
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🖼️ PHOTO D'ACCUEIL — METS TON LIEN JPEG ICI
PHOTO_START_URL = "https://image2url.com/images/1763587287262-54768308-b40a-4f85-93fd-32ddce56375e.jpeg"


# -------------------------
#      COMMANDE /START
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [

        # Ligne 1
        [
            InlineKeyboardButton("Informations ℹ️", callback_data="info"),
            InlineKeyboardButton("Contact 📱", callback_data="contact")
        ],

        # Ligne 2 — Mini-App
        [
            InlineKeyboardButton("Mini-App 🎮", url="https://grosbagel93-cell.github.io/La-stuperie74/")
        ],

        # Ligne 3 — Lien provisoire (pas d'erreur)
        [
            InlineKeyboardButton("Telegram 📺", url="https://google.com"),
            InlineKeyboardButton("Snapchat 👻", url="https://google.com")
        ],

        # Ligne 4 — Lien provisoire
        [
            InlineKeyboardButton("Potato 🥔", url="https://google.com"),
            InlineKeyboardButton("Instagram 📸", url="https://google.com")
        ],

        # Ligne 5 — Lien provisoire
        [
            InlineKeyboardButton("Linkbio 🔗", url="https://google.com")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=PHOTO_START_URL,
        caption=(
            "BONJOUR À TOUS 👋\n\n"
            "Bienvenue sur notre BOT Officiel 🤖\n\n"
            "Clique sur « Mini-App » pour accéder au menu 🎮📍"
        ),
        reply_markup=reply_markup
    )


# -------------------------
#        CALLBACKS MENU
# -------------------------

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_caption(
            "ℹ️ Informations :\n\n"
            "Tu peux modifier ce message dans le bot."
        )

    elif query.data == "contact":
        await query.edit_message_caption(
            "📞 Contact :\n\n"
            "Tu peux mettre ton contact ici."
        )


# -------------------------
#        LANCEMENT BOT
# -------------------------

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()


if __name__ == "__main__":
    main()