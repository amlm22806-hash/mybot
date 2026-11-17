import os
import telebot

from telebot import types

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(message.chat.id, 'أهلاً بك 👋\nاختر من الأزرار بالأسفل:')
    except:
        pass
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton("ℹ️ مساعدة", callback_data="help")
   
    btn3 = types.InlineKeyboardButton("USDT", callback_data="usdt_btn")
    markup.add(btn2, btn3)
    bot.reply_to(message, "اضغط USDT واعمل الخطوات التاليه", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "send_link")
def ask_name(call):
    bot.send_photo(call.message.chat.id, "https://رابط-صورتك-هنا", caption="هذي الخطوات")
    bot.register_next_step_handler(call.message, get_name)

def get_name(message):
    users[message.from_user.id] = message.text

@bot.callback_query_handler(func=lambda call: call.data == "help")
def help_cb(call):
    pass

def show_links(message):
    try:
        with open("links.txt", "r") as f:
            data = f.read()
        if not data:
            bot.reply_to(message, "مافي روابط للحين")
        else:
            bot.reply_to(message, "الروابط المحفوظة:\n\n" + data)
    except:
        bot.reply_to(message, "مافي روابط للحين")

@bot.message_handler(func=lambda m: "t.me/" in (m.text or ""))
def save(message):
    name = users.get(message.from_user.id, "بدون اسم")
    with open("links.txt", "a") as f:
        f.write(f"{name} : {message.text}\n")
    bot.reply_to(message, f"تم حفظ رابطك يا {name}! ✅")
@bot.callback_query_handler(func=lambda call: call.data == "usdt_btn")
def usdt_cb(call):
    bot.send_message(call.message.chat.id, "USDT on BNB Chain\n\n1 - Open MetaMask\n2 - Tap Tokens\n3 - Choose BNB Chain\n4 - Tap Import Tokens\n5 - Paste contract below\n6 - Tap Import\n\nContract / العقد:\n0x55d398326f99059fF775485246999027B3197955\n\n---\nUSDT على شبكة BNB\n\n1 - افتح محفظة MetaMask\n2 - اضغط على Tokens\n3 - اختر شبكة BNB Chain\n4 - اضغط على Import Tokens\n5 - الصق العقد بالأسفل\n6 - اضغط على Import\n\nالعقد:\n0x55d398326f99059fF775485246999027B3197955")
    try:
        bot.send_photo(call.message.chat.id, open('photo.jpg','rb'))
    except Exception as e:
        print('PHOTO ERROR:', e)
    bot.send_message(call.message.chat.id, "0x55d398326f99059fF775485246999027B3197955")
    bot.send_message(call.message.chat.id, "Send your wallet address after")
print("Bot is running...")
@bot.message_handler(commands=['usdt'])
def usdt(message):
    bot.send_message(message.chat.id, "USDT on BNB Chain\n\n1 - Open MetaMask\n2 - Tap Tokens\n3 - Choose BNB Chain\n4 - Tap Import Tokens\n5 - Paste contract below\n6 - Tap Import\n\nContract / العقد:\n0x55d398326f99059fF775485246999027B3197955\n\n---\nUSDT على شبكة BNB\n\n1 - افتح محفظة MetaMask\n2 - اضغط على Tokens\n3 - اختر شبكة BNB Chain\n4 - اضغط على Import Tokens\n5 - الصق العقد بالأسفل\n6 - اضغط على Import\n\nالعقد:\n0x55d398326f99059fF775485246999027B3197955")
    try:
        bot.send_photo(message.chat.id, open('photo.jpg','rb'))
    except Exception as e:
        print('PHOTO ERROR:', e)
    bot.send_message(message.chat.id, "0x55d398326f99059fF775485246999027B3197955")
    bot.send_message(message.chat.id, "Send your wallet address after")
bot.infinity_polling()
