from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import random
import os

# توكن البوت
TOKEN = "7808404443:AAEbwuhSc-5aiUvaH3HhXlJIOmsCKYJV1O8"

# دالة لإنشاء ملف requirements.txt
def create_requirements_file():
    requirements = """python-telegram-bot==20.3"""
    with open("requirements.txt", "w") as file:
        file.write(requirements)

# دالة لبدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # حذف الرسائل القديمة إذا كانت موجودة
    if context.user_data.get("last_message_id"):
        try:
            await context.bot.delete_message(
                chat_id=update.message.chat_id,
                message_id=context.user_data["last_message_id"]
            )
        except:
            pass  # إذا لم يتم العثور على الرسالة، تجاهل الخطأ

    # إنشاء خيارات الأزرار
    keyboard = [
        [InlineKeyboardButton("❤️ نسبة حب كركر لك ❤️", callback_data='love')],
        [InlineKeyboardButton("🐐 هل أنتِ صخل أم طلي 🐑", callback_data='animal')],
        [InlineKeyboardButton("💌 ماذا تعنين لكروري 💌", callback_data='meaning')],
        [InlineKeyboardButton("😘 هل تريدين بوسة من كروري؟ 😘", callback_data='kiss')],
        [InlineKeyboardButton("🤗 هل تريدين حضنة من كيرلو؟ 🤗", callback_data='hug')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # رسالة الترحيب الجديدة
    message = await update.message.reply_text(
        "👋 أهلاً وسهلاً بك في بوت كركر!\nاختر أحد الخيارات أدناه 👇:",
        reply_markup=reply_markup
    )

    # حفظ ID الرسالة الأخيرة
    context.user_data["last_message_id"] = message.message_id

# دالة لمعالجة الاختيارات
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # تأكيد الضغط

    if query.data == 'love':
        # نسبة حب عشوائية بين 95 و 100
        love_percentage = random.randint(95, 100)
        await query.edit_message_text(
            f"❤️ نسبة حب كركر لك هي: {love_percentage}% ❤️\nكركر يحبك جداً! 😍"
        )
    elif query.data == 'animal':
        # اختيار عشوائي بين "صخل" و "طلي"
        animal = random.choice(["🐐 نعم، أنتِ صخل! 😂", "🐑 نعم، أنتِ طلي! 😅"])
        await query.edit_message_text(animal)
    elif query.data == 'meaning':
        # اختيار عشوائي من قائمة معاني
        meanings = [
            "❤️ كروري يحبك كثيراً لكن حضرتك هايشة 🐄😂",
            "💕 كركر يعشقكِ يا أم رأس 🤣",
            "😍 أبو الكوك يحب الهايشة حوراء 🐮😂"
        ]
        meaning = random.choice(meanings)
        await query.edit_message_text(meaning)
    elif query.data == 'kiss':
        # إنشاء كلمة "مممحححححححح" مع عدد عشوائي من الحروف
        extra_h = "ح" * random.randint(3, 10)
        kiss_message = f"مممح{extra_h} 😘"
        await query.edit_message_text(kiss_message)
    elif query.data == 'hug':
        # إرسال رسالة حضن مع سمايلات
        hug_message = "🤗 كروري يعطيكِ أكبر حضن مليان حب! 💖🤗"
        await query.edit_message_text(hug_message)

# الدالة الرئيسية لتشغيل البوت
def main():
    # إنشاء ملف requirements.txt
    create_requirements_file()

    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()

    # إضافة الأوامر والمعالجات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # بدء البوت
    application.run_polling()

if __name__ == "__main__":
    main()
