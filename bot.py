# -*- coding: utf-8 -*-
import telebot
from telebot import types

# ضع رمز التوكن الخاص ببوتك هنا الذي حصلت عليه من @BotFather
BOT_TOKEN = "8699837750:AAEHxpnd_Xw26jsrHFTYwVImd39Pu-sC554"

bot = telebot.TeleBot(BOT_TOKEN)

# رابط موقع اللعبة المباشر الخاص بك
WEBSITE_URL = "https://ais-pre-ntggp355r6qq6elhc6sbed-485747710736.europe-west1.run.app"

# رسالة الترحيب الأنيقة عند كتابة /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    btn_download = types.InlineKeyboardButton("📥 تحميل لعبة LuxeMines APK", callback_data="download_apk")
    btn_website = types.InlineKeyboardButton("🌐 زيارة الموقع الرسمي الفاخر", url=WEBSITE_URL)
    btn_deposit = types.InlineKeyboardButton("💳 طريقة شحن الرصيد والـ DZD", callback_data="deposit_info")
    btn_withdraw = types.InlineKeyboardButton("💸 طريقة سحب الأرباح الفورية", callback_data="withdraw_info")
    btn_support = types.InlineKeyboardButton("☎️ التواصل مع الدعم الفني المباشر", callback_data="support_contact")
    
    markup.add(btn_download, btn_website, btn_deposit, btn_withdraw, btn_support)
    
    welcome_text = (
        "💎 *أهلاً بك في منصة LuxeMines الراقية!* 💎\n\n"
        "أنت الآن متصل بالبوت المساعد الرسمي للعبة الألغام الفاخرة بالدينار الجزائري (DZD).\n\n"
        "🔥 *ماذا يمكنك أن تفعل هنا؟*\n"
        "• تحميل اللعبة الرسمية مباشرة للأندرويد.\n"
        "• الحصول على بونص 100% عند الإيداع الأول.\n"
        "• الاستفسار عن شحن رصيدك أو سحب أرباحك بالدينار الجزائري عبر بريدي أو كاش أو الدعم المباشر.\n\n"
        "👇 اختر من الخيارات أدناه لبدء المغامرة وجني المكاسب الحقيقية:"
    )
    
    bot.reply_to(message, welcome_text, parse_mode="Markdown", reply_markup=markup)

# معالجة الضغط على الأزرار التفاعلية (Callbacks)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "download_apk":
        # عرض روابط التحميل المباشرة
        markup = types.InlineKeyboardMarkup()
        btn_direct = types.InlineKeyboardButton("📥 تحميل APK مباشر", url=f"{WEBSITE_URL}/LuxeMines.apk")
        btn_back = types.InlineKeyboardButton("🔙 العودة للقائمة", callback_data="back_main")
        markup.add(btn_direct)
        markup.add(btn_back)
        
        text = (
            "🚀 *تحميل تطبيق LuxeMines الرسمي للأندرويد*\n\n"
            "اضغط على زر التحميل المباشر أدناه لتنزيل ملف الـ APK وتثبيته فوراً!\n\n"
            "💡 *ملاحظة عند التثبيت:*\n"
            "إذا ظهر لك تنبيه 'مصادر غير معروفة'، توجه إلى الإعدادات وقم بالسماح للمتصفح بتثبيت التطبيقات لتستمتع باللعبة وصلاحيتها الكاملة."
        )
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    elif call.data == "deposit_info":
        markup = types.InlineKeyboardMarkup()
        btn_chat_support = types.InlineKeyboardButton("💬 تواصل لشحن رصيدي الآن", url="https://t.me/your_telegram_username") # غير هذا المعرف بمعرف حسابك الشخصي
        btn_back = types.InlineKeyboardButton("🔙 العودة", callback_data="back_main")
        markup.add(btn_chat_support)
        markup.add(btn_back)
        
        text = (
            "💳 *طريقة شحن الرصيد لتفعيل بونص 100%:* 💳\n\n"
            "1️⃣ نقبل جميع طرق الدفع السهلة والشائعة في الجزائر (Baridimob، CCP، وغيرها من المحافظ الإلكترونية).\n"
            "2️⃣ تواصل مع الوكيل أو المشرف المالي عبر التليجرام لشحن الحساب وإرسال الوصل الثبوتي.\n"
            "3️⃣ سيتم شحن حسابك في أقل من 5 دقائق وتفعيل البونص الـ 100% تلقائياً لتتمكن من رفع رهاناتك وكشف الجواهر!\n\n"
            "اضغط على الزر للتحدث المباشر مع المسؤول الفني والشحن:"
        )
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    elif call.data == "withdraw_info":
        markup = types.InlineKeyboardMarkup()
        btn_chat_support = types.InlineKeyboardButton("💸 طلب سحب الأرباح", url="https://t.me/your_telegram_username")
        btn_back = types.InlineKeyboardButton("🔙 العودة", callback_data="back_main")
        markup.add(btn_chat_support)
        markup.add(btn_back)
        
        text = (
            "💸 *طريقة سحب أرباحك الحقيقية بالـ DZD:* 💸\n\n"
            "تتميز LuxeMines بنظام سحب أوتوماتيكي ومبسط لضمان استلام أموالك:\n\n"
            "🔗 *الخطوات:*\n"
            "1. افتح تطبيق LuxeMines وتوجه لقسم المحفظة (Wallet).\n"
            "2. اضغط على طلب السحب واكتب محفظتك ورقم Baridimob الخاص بك.\n"
            "3. أو تواصل فوراً هنا معنا وقم بإرسال معرّف حسابك الإلكتروني لحسم الأرباح وتحويلها لـ CCP الخاص بك دفعة واحدة!\n\n"
            "🌟 نلتزم بنسبة سداد ومصداقية 100%!"
        )
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    elif call.data == "support_contact":
        markup = types.InlineKeyboardMarkup()
        btn_chat_support = types.InlineKeyboardButton("📬 التحدث مع ممثل الدعم المالي", url="https://t.me/your_telegram_username")
        btn_back = types.InlineKeyboardButton("🔙 العودة", callback_data="back_main")
        markup.add(btn_chat_support)
        markup.add(btn_back)
        
        text = (
            "☎️ *قسم الدعم الفني والمساعدة:* ☎️\n\n"
            "نحن هنا لخدمتك على مدار الساعة، تفضل بطرح استفسارك بخصوص:\n"
            "• تأخر وصول الإيداع أو السحب.\n"
            "• مشاكل تقنية أثناء تشغيل اللعبة على هاتف الأندرويد.\n"
            "• رغبتك في حجز عروض وبونص حصرية للاعبين الـ VIP.\n\n"
            "راسلنا وسنرد عليك في غضون ثوانٍ معدودة!"
        )
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        
    elif call.data == "back_main":
        # العودة للقائمة الرئيسية
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn_download = types.InlineKeyboardButton("📥 تحميل لعبة LuxeMines APK", callback_data="download_apk")
        btn_website = types.InlineKeyboardButton("🌐 زيارة الموقع الرسمي الفاخر", url=WEBSITE_URL)
        btn_deposit = types.InlineKeyboardButton("💳 طريقة شحن الرصيد والـ DZD", callback_data="deposit_info")
        btn_withdraw = types.InlineKeyboardButton("💸 طريقة سحب الأرباح الفورية", callback_data="withdraw_info")
        btn_support = types.InlineKeyboardButton("☎️ التواصل مع الدعم الفني المباشر", callback_data="support_contact")
        
        markup.add(btn_download, btn_website, btn_deposit, btn_withdraw, btn_support)
        
        welcome_text = (
            "💎 *أهلاً بك في منصة LuxeMines الراقية!* 💎\n\n"
            "أنت الآن متصل بالبوت المساعد الرسمي للعبة الألغام الفاخرة بالدينار الجزائري (DZD).\n\n"
            "👇 اختر من الخيارات أدناه لبدء المغامرة وجني المكاسب الحقيقية:"
        )
        bot.edit_message_text(welcome_text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)

# تشغيل البوت بشكل مستمر للاستجابة السريعة
if __name__ == '__main__':
    print("💎 LuxeMines Telegram Bot has successfully started listening...")
    bot.infinity_polling()
