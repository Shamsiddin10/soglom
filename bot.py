import telebot
from telebot import types
import random

TOKEN = '8721754529:AAHJTsDMcJzV0y5QoIeF0TnCUty8WrXxG5Y'
bot = telebot.TeleBot(TOKEN)

# Motivatsion so'zlar ro'yxati
motivations = [
    "Sog'ligingiz – sizning eng katta boyligingiz. Uni asrang! ✨",
    "Kichik qadamlar bilan katta natijalarga erishish mumkin. Bugun sport qildingizmi? 🏃",
    "Har bir yegan sog'lom ovqatingiz – kelajagingiz uchun sarmoyadir! 🥗",
    "Kulgi va ijobiy kayfiyat eng yaxshi doridir! Bugun tabassum qilishni unutmang 😊",
    "O'z tanangizni seving va u sizga uzoq yillar xizmat qiladi! 💖"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("💧 Suv ichish eslatmasi")
    btn2 = types.KeyboardButton("🍎 Sog'lom ovqatlanish")
    btn3 = types.KeyboardButton("🏃‍♂️ Jismoniy mashqlar")
    btn4 = types.KeyboardButton("😴 Uyqu rejimi")
    btn5 = types.KeyboardButton("💪 Kunlik motivatsiya")
    btn6 = types.KeyboardButton("💊 Vitaminlar haqida")
    btn7 = types.KeyboardButton("🩺 Shifokor eslatmasi")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    
    bot.send_message(message.chat.id, 
                     "Assalomu alaykum! Men kengaytirilgan sog'lom turmush tarzi botiman. 🍏\n\n"
                     "Sizga yanada ko'proq foydali ma'lumotlar bera olaman. "
                     "Kerakli bo'limni tanlang:", 
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text
    
    if text == "💧 Suv ichish eslatmasi":
        bot.send_message(message.chat.id, 
                         "💧 **Suv inson tanasi uchun juda muhim!**\n\n"
                         "Har kuni o'rtacha 2-2.5 litr suv ichishni unutmang.\n\n"
                         "💡 *Maslahat:* Har kuni ertalab uyg'onndeganingizda 1-2 stakan iliq suv ichishni odat qiling.", parse_mode="Markdown")
        
    elif text == "🍎 Sog'lom ovqatlanish":
        bot.send_message(message.chat.id, 
                         "🍎 **Sog'lom ovqatlanish - mustahkam sog'liq garovi!**\n\n"
                         "- Ko'proq meva va sabzavotlar iste'mol qiling.\n"
                         "- Fast-food va shirinliklarni kamaytiring.\n"
                         "- Kechki ovqatni uxlashdan 2-3 soat oldin yeng.", parse_mode="Markdown")
        
    elif text == "🏃‍♂️ Jismoniy mashqlar":
        bot.send_message(message.chat.id, 
                         "🏃‍♂️ **Harakatda - barakat!**\n\n"
                         "- Har kuni kamida 30 daqiqa piyoda yuring.\n"
                         "- Ertalabki badantarbiya mashqlarini bajaring.\n"
                         "- Haftada 2-3 marta sport zaliga boring.", parse_mode="Markdown")
        
    elif text == "😴 Uyqu rejimi":
        bot.send_message(message.chat.id, 
                         "😴 **Yaxshi uyqu - asab tizimini tiklaydi!**\n\n"
                         "- 7-8 soat uxlash tavsiya etiladi.\n"
                         "- Uxlashdan 1 soat oldin telefondan foydalanmang.", parse_mode="Markdown")

    elif text == "💪 Kunlik motivatsiya":
        quote = random.choice(motivations)
        bot.send_message(message.chat.id, f"🌟 **Kunlik Motivatsiya:**\n\n_{quote}_", parse_mode="Markdown")
        
    elif text == "💊 Vitaminlar haqida":
        bot.send_message(message.chat.id, 
                         "💊 **Muhim Vitaminlar va ularning manbalari:**\n\n"
                         "☀️ **Vitamin D:** Quyosh nuri, tuxum sarig'i, baliq.\n"
                         "🍊 **Vitamin C:** Apelsin, limon, kivi, bulg'or qalampiri.\n"
                         "🥩 **Vitamin B12:** Go'sht, sut mahsulotlari.\n"
                         "🥕 **Vitamin A:** Sabzi, oshqovoq, ismaloq.\n\n"
                         "⚠️ _Eslatma: Vitaminlarni ichishdan oldin shifokor bilan maslahatlashing._", parse_mode="Markdown")
        
    elif text == "🩺 Shifokor eslatmasi":
        bot.send_message(message.chat.id, 
                         "🩺 **Sog'likni tekshirtirish:**\n\n"
                         "O'zingizni yaxshi his qilsangiz ham, yilda kamida 1 marta to'liq tibbiy ko'rikdan (chek-ap) o'tishni unutmang. \n\n"
                         "Qon tahlillari va tish shifokori ko'rigi kelajakdagi ko'p muammolarning oldini oladi! 🏥", parse_mode="Markdown")
        
    else:
        bot.send_message(message.chat.id, "Kechirasiz, men tushunmadim. Iltimos, pastdagi menyudan foydalaning.")

print("Bot ishga tushdi...")
bot.polling(none_stop=True)
