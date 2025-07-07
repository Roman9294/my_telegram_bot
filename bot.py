from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TOKEN  # Імпортуємо токен з окремого файлу

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    bonus_url = "https://1whecs.life/?p=8h10"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎁 ЗАБРАТЬ БОНУС", url=bonus_url)]
    ])

    with open("photo_2.jpg", "rb") as photo:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption="Нажми кнопку ниже, чтобы забрать бонус 🎉",
            reply_markup=keyboard
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот працює!")
    app.run_polling()
