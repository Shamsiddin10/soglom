import telebot
from telebot import types

# O'zingizning bot tokeningizni shu yerga kiriting
TOKEN =("8721754529:AAHJTsDMcJzV0y5QoIeF0TnCUty8WrXxG5Y")
bot = telebot.TeleBot(TOKEN)

# /start buyrug'i bosilganda ishlaydigan qism
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Tugmalarni yaratish
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("💧 Suv ichish eslatmasi")
    btn2 = types.KeyboardButton("🍎 Sog'lom ovqatlanish")
    btn3 = types.KeyboardButton("🏃‍♂️ Jismoniy mashqlar")
    btn4 = types.KeyboardButton("😴 Uyqu rejimi")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(message.chat.id, 
                     "Assalomu alaykum! Men sog'lom turmush tarzi botiman. 🍏\n\n"
                     "Sizga o'z sog'ligingizni asrashda yordam beraman. "
                     "Kerakli bo'limni tanlang:", 
                     reply_markup=markup)

# Matnli xabarlarga javob berish
@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text
    
    if text == "💧 Suv ichish eslatmasi":
        bot.send_message(message.chat.id, 
                         "💧 **Suv inson tanasi uchun juda muhim!**\n\n"
                         "Har kuni o'rtacha 2-2.5 litr (yoki tana vazningizga qarab har 1 kg uchun 30 ml) suv ichishni unutmang.\n\n"
                         "💡 *Maslahat:* Har kuni ertalab uyg'onganingizda 1-2 stakan iliq suv ichishni odat qiling. Bu organizmni uyg'otadi va moddalar almashinuvini yaxshilaydi.", parse_mode="Markdown")
        
    elif text == "🍎 Sog'lom ovqatlanish":
        bot.send_message(message.chat.id, 
                         "🍎 **Sog'lom ovqatlanish - mustahkam sog'liq garovi!**\n\n"
                         "- Ko'proq meva va sabzavotlar iste'mol qiling.\n"
                         "- Fast-food, gazli ichimliklar va shirinliklarni kamaytiring.\n"
                         "- Kechki ovqatni uxlashdan kamida 2-3 soat oldin yeng va yengil ovqatlarni tanlang.", parse_mode="Markdown")
        
    elif text == "🏃‍♂️ Jismoniy mashqlar":
        bot.send_message(message.chat.id, 
                         "🏃‍♂️ **Harakatda - barakat!**\n\n"
                         "- Har kuni kamida 30 daqiqa ochiq havoda piyoda yuring.\n"
                         "- Ertalabki badantarbiya mashqlarini bajaring.\n"
                         "- Agar imkoningiz bo'lsa, haftada 2-3 marta sport zaliga, yugurishga yoki suzishga boring.\n"
                         "- Uzoq vaqt o'tirib ishlasangiz, har soatda 5-10 daqiqa tanaffus qilib, chigalyozdi mashqlarini bajaring.", parse_mode="Markdown")
        
    elif text == "😴 Uyqu rejimi":
        bot.send_message(message.chat.id, 
                         "😴 **Yaxshi uyqu - asab tizimini tiklaydi!**\n\n"
                         "- Kattalar uchun o'rtacha 7-8 soat uxlash tavsiya etiladi.\n"
                         "- Har kuni bir xil vaqtda uxlashga va uyg'onishga harakat qiling.\n"
                         "- Uxlashdan 1 soat oldin telefon, kompyuter va televizordan foydalanmang (ko'k chiroq uyqu gormoniga xalaqit beradi).", parse_mode="Markdown")
        
    else:
        bot.send_message(message.chat.id, "Kechirasiz, men tushunmadim. Iltimos, menyudagi tugmalardan birini bosib tanlang.")

# Botni doimiy ishlab turishi uchun
print("Bot ishga tushdi...")
bot.polling(none_stop=True)
