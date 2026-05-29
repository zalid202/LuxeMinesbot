const TelegramBot = require('node-telegram-bot-api');

// ضع رمز التوكن الخاص ببوتك هنا الذي حصلت عليه من @BotFather
const token = '8699837750:AAEHxpnd_Xw26jsrHFTYwVImd39Pu-sC554';

// رابط موقع اللعبة المباشر الخاص بك
const WEBSITE_URL = 'https://ais-pre-ntggp355r6qq6elhc6sbed-485747710736.europe-west1.run.app';
const MAIN_SUPPORT_TELEGRAM = 'https://t.me/your_telegram_username'; // معرّف حسابك لتلقي الرسائل

const bot = new TelegramBot(token, { polling: true });

console.log('💎 LuxeMines Node.js Telegram Bot started successfully and listening...');

// قائمة الأزرار الرئيسية
const mainKeyboard = {
    reply_markup: {
        inline_keyboard: [
            [{ text: '📥 تحميل لعبة LuxeMines APK', callback_data: 'download_apk' }],
            [{ text: '🌐 زيارة الموقع الرسمي الفاخر', url: WEBSITE_URL }],
            [{ text: '💳 طريقة شحن الرصيد والـ DZD', callback_data: 'deposit_info' }],
            [{ text: '💸 طريقة سحب الأرباح الفورية', callback_data: 'withdraw_info' }],
            [{ text: '☎️ التواصل مع الدعم الفني المباشر', callback_data: 'support_contact' }]
        ]
    }
};

// النقر على أمر /start
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const welcomeText = 
`💎 *أهلاً بك في منصة LuxeMines الراقية!* 💎

أنت الآن متصل بالبوت المساعد الرسمي للعبة الألغام الفاخرة بالدينار الجزائري (DZD).

🔥 *ماذا يمكنك أن تفعل هنا؟*
• تحميل اللعبة الرسمية مباشرة للأندرويد.
• الحصول على بونص 100% عند الإيداع الأول.
• الاستفسار عن شحن رصيدك أو سحب أرباحك بالدينار الجزائري عبر بريدي أو كاش أو الدعم المباشر.

👇 اختر من الخيارات أدناه لبدء المغامرة وجني المكاسب الحقيقية:`;

    bot.sendMessage(chatId, welcomeText, { parse_mode: 'Markdown', ...mainKeyboard });
});

// معالجة الضغط على الأزرار التفاعلية
bot.on('callback_query', (callbackQuery) => {
    const action = callbackQuery.data;
    const msg = callbackQuery.message;
    const opts = {
        chat_id: msg.chat.id,
        message_id: msg.message_id,
        parse_mode: 'Markdown'
    };

    if (action === 'download_apk') {
        const text = 
`🚀 *تحميل تطبيق LuxeMines الرسمي للأندرويد*

اضغط على زر التحميل المباشر أدناه لتنزيل ملف الـ APK وتثبيته فوراً!

💡 *ملاحظة عند التثبيت:*
إذا ظهر لك تنبيه 'مصادر غير معروفة'، توجه إلى الإعدادات وقم بالسماح للمتصفح بتثبيت التطبيقات لتستمتع باللعبة وصلاحيتها الكاملة.`;

        bot.editMessageText(text, {
            ...opts,
            reply_markup: {
                inline_keyboard: [
                    [{ text: '📥 تحميل APK مباشر', url: `${WEBSITE_URL}/LuxeMines.apk` }],
                    [{ text: '🔙 العودة للقائمة', callback_data: 'back_main' }]
                ]
            }
        });
    } else if (action === 'deposit_info') {
        const text = 
`💳 *طريقة شحن الرصيد لتفعيل بونص 100%:* 💳

1️⃣ نقبل جميع طرق الدفع السهلة والشائعة في الجزائر (Baridimob، CCP، وغيرها من المحافظ الإلكترونية).
2️⃣ تواصل مع الوكيل أو المشرف المالي عبر التليجرام لشحن الحساب وإرسال الوصل الثبوتي.
3️⃣ سيتم شحن حسابك في أقل من 5 دقائق وتفعيل البونص الـ 100% تلقائياً لتتمكن من رفع رهاناتك وكشف الجواهر!

اضغط على الزر للتحدث المباشر مع المسؤول الفني والشحن:`;

        bot.editMessageText(text, {
            ...opts,
            reply_markup: {
                inline_keyboard: [
                    [{ text: '💬 تواصل لشحن رصيدي الآن', url: MAIN_SUPPORT_TELEGRAM }],
                    [{ text: '🔙 العودة', callback_data: 'back_main' }]
                ]
            }
        });
    } else if (action === 'withdraw_info') {
        const text = 
`💸 *طريقة سحب أرباحك الحقيقية بالـ DZD:* 💸

تتميز LuxeMines بنظام سحب أوتوماتيكي ومبسط لضمان استلام أموالك:

🔗 *الخطوات:*
1. افتح تطبيق LuxeMines وتوجه لقسم المحفظة (Wallet).
2. اضغط على طلب السحب واكتب محفظتك ورقم Baridimob الخاص بك.
3. أو تواصل فوراً هنا معنا وقم بإرسال معرّف حسابك الإلكتروني لحسم الأرباح وتحويلها لـ CCP الخاص بك دفعة واحدة!

🌟 نلتزم بنسبة سداد ومصداقية 100%!`;

        bot.editMessageText(text, {
            ...opts,
            reply_markup: {
                inline_keyboard: [
                    [{ text: '💸 طلب سحب الأرباح', url: MAIN_SUPPORT_TELEGRAM }],
                    [{ text: '🔙 العودة', callback_data: 'back_main' }]
                ]
            }
        });
    } else if (action === 'support_contact') {
        const text = 
`☎ *قسم الدعم الفني والمساعدة:* ☎

نحن هنا لخدمتك على مدار الساعة، تفضل بطرح استفسارك بخصوص:
• تأخر وصول الإيداع أو السحب.
• مشاكل تقنية أثناء تشغيل اللعبة على هاتف الأندرويد.
• رغبتك في حجز عروض وبونص حصرية للاعبين الـ VIP.

راسلنا وسنرد عليك في غضون ثوانٍ معدودة!`;

        bot.editMessageText(text, {
            ...opts,
            reply_markup: {
                inline_keyboard: [
                    [{ text: '📬 التحدث مع ممثل الدعم المالي', url: MAIN_SUPPORT_TELEGRAM }],
                    [{ text: '🔙 العودة', callback_data: 'back_main' }]
                ]
            }
        });
    } else if (action === 'back_main') {
        const welcomeText = 
`💎 *أهلاً بك في منصة LuxeMines الراقية!* 💎

أنت الآن متصل بالبوت المساعد الرسمي للعبة الألغام الفاخرة بالدينار الجزائري (DZD).

👇 اختر من الخيارات أدناه لبدء المغامرة وجني المكاسب الحقيقية:`;

        bot.editMessageText(welcomeText, {
            ...opts,
            reply_markup: mainKeyboard.reply_markup
        });
    }
});
