import telebot
from config import currencies, TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

#Реакция на команду /start или /help - вывод инструкции по применению бота
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту в следующем формате:\n<имя валюты> <в какую валюту перевести> <количество переводимой валюты> \nУвидеть список всех доступных валют: /values \nПосмотреть пример запроса к боту: /example'
    bot.reply_to(message, text)

#Реакция на команду /values - вывод доступных валют
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currencies.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

#Реакция на команду /example
@bot.message_handler(commands=['example'])
def values(message: telebot.types.Message):
    text = 'Пример ввода: \nдоллар рубль 15'
    bot.reply_to(message, text)


#Логика работы бота:
@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    #Проверка на количество переданных параметров
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Допустимое количество параметров: 3')

        quote, base, amount = values

        #Получаем данные:
        total_base = CurrencyConverter.get_price(quote, base, amount)
    #Иные ошибки пользователя   
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')
    else:
    #Если все в порядке - выводим полученные данные
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop=True, interval=0)