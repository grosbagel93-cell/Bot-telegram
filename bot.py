import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# 🔑 Ton token récupéré automatiquement par Render
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🖼️ PHOTO D'ACCUEIL — METS TON LIEN JPEG !!!
PHOTO_START_URL = "https://image2url.com/images/1763587287262-54768308-b40a-4f85-93fd-32ddce56375e.jpeg"
# Remplace par ton lien d’image quand tu veux


# -------------------------
#      COMMANDE /START
# -------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # ⚡ MENU EXACTEMENT COMME SUR TA PHOTO
    keyboard = [

        # Ligne 1
        [
            InlineKeyboardButton("Informations ℹ️", callback_data="info"),
            InlineKeyboardButton("Contact 📱", callback_data="contact")
        ],

        # Ligne 2 — Bouton Mini-App
        [
            InlineKeyboardButton("Mini-App 🎮", url="https://grosbagel93-cell.github.io/La-stuperie74/")
        ],

        # Ligne 3
        [
            InlineKeyboardButton("Telegram 📺", url="https://TON_LIEN_TELEGRAM"),
            InlineKeyboardButton("Snapchat 👻", url="https://TON_LIEN_SNAPCHAT")
        ],

        # Ligne 4
        [
            InlineKeyboardButton("Potato 🥔", url="https://TON_LIEN_POTATO"),
            InlineKeyboardButton("Instagram 📸", url="https://TON_LIEN_INSTAGRAM")
        ],

        # Ligne 5
        [
            InlineKeyboardButton("Linkbio 🔗", url="https://TON_LINKBIO")
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
#       CALLBACKS MENU
# -------------------------

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_caption(
            "ℹ️ Informations :\n\n"
            "(Modifie ce texte comme tu veux)"
        )

    elif query.data == "contact":
        await query.edit_message_caption(
            "📞 Contact :\n\n"
            "(Mets ici ton contact)"
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
