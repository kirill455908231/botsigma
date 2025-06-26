import telebot 
from Config import TG_TOKEN  # type: ignore


bot = telebot.TeleBot(TG_TOKEN) 


# @bot.message_handler(КРИТЕРИЙ_ОБРАБОТКИ) 
# def ...(message):
#     .... 

# 1 критерий - команды 
@bot.message_handler(commands=['start' , 'help']) #/start, /help
def start_command(message):
    bot.send_message(message.chat.id, 'Привет,  пользавотель! ') 


#2 критерий - тип сообщения 
@bot.message_handler(content_types=['sticker']) # 'audio', 'photo', 'voice',  'video', 'document',  'text', 'look'
def handle_sticker(message):
    bot.reply_to(message, 'Вау,  какой крутой стикер! ') 

# 3 критерий - лямбда-функция (собственный критерий) 
@bot.message_handler(func=lambda message: 'блин' in message.text.lower()) 
def handler_blin(message):
    bot.reply_to(message, f' слушай, {message.from_user.first_name}, я люблю блины') #json viewer 

bot.infinity_polling()
