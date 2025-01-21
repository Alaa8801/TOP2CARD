
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Initialize the bot with the provided token
TOKEN = "7567421426:AAGLAiAGw2a9utgaCmnSEDx0raZ0WGc9OvY"
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Start command handler
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("PUBG", callback_data="pubg")],
        [InlineKeyboardButton("Free Fire", callback_data="free_fire")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("مرحباً بك! اختر الخدمة التي ترغب بها:", reply_markup=reply_markup)

# Callback query handler
def handle_menu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "pubg":
        keyboard = [
            [InlineKeyboardButton("أكواد", callback_data="pubg_codes")],
            [InlineKeyboardButton("ID", callback_data="pubg_id")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("اختر الطريقة:", reply_markup=reply_markup)

    elif query.data == "pubg_id":
        keyboard = [
            [InlineKeyboardButton("60 شدة", callback_data="pubg_60")],
            [InlineKeyboardButton("325 شدة", callback_data="pubg_325")],
            [InlineKeyboardButton("660 شدة", callback_data="pubg_660")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("اختر الفئة:", reply_markup=reply_markup)

    elif query.data in ["pubg_60", "pubg_325", "pubg_660"]:
        query.edit_message_text(
            f"تم اختيارك لفئة {query.data.split('_')[1]} شدة.
"
            "يرجى متابعة عملية الدفع عبر الرابط التالي:
"
            "[رابط الدفع بالعملات الرقمية](https://example.com/payment)",
            parse_mode="Markdown",
        )
        # Notify the admin (replace with your Telegram ID)
        admin_id = "YOUR_ADMIN_ID"
        context.bot.send_message(
            chat_id=admin_id,
            text=f"طلب جديد:
الخدمة: بوبجي
الفئة: {query.data.split('_')[1]} شدة.
يرجى الموافقة عليه."
        )

# Add handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(handle_menu))

# Start the bot
updater.start_polling()
