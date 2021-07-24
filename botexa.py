import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1939296793:AAFrCb56ZfkW-psVP1-bQhMK1sp6wiy9OLs') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['info']) #definimos el comando
def info(mensaje):
    bot.reply_to(mensaje, get_me)
    print("Mandaron info")
@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "Hola como estás?")
    print("Mandaron hola o hi")
@bot.message_handler(commands=['conversion', 'conversion'])
def conversion(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('C:/Users/Dios es Amor/Desktop/exa/conversion.png', 'rb')
    bot.send_photo(id, photo)
@bot.message_handler(commands=['cuadratica', 'cuadratica'])
def cuadratica(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('C:/Users/Dios es Amor/Desktop/exa/formula cuadratuca.jpg', 'rb')
    bot.send_photo(id, photo)
@bot.message_handler(commands=['documento', 'pdf'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    document = open('C:/Users/Dios es Amor/Desktop/exa/escritura normalizada 2.pdf', 'rb')
    bot.send_document(id, document)
@bot.message_handler(commands=['ubicacion'])
def ubicacion(mensaje):
    bot.send_chat_action(id, 'find_location')
    bot.send_location(id, 15.495643952933062, -87.9912972211749)
bot.polling()