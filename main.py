import telebot
import requests
import json
import datetime

bot = telebot.TeleBot('7872698112:AAFDVCXbxSG3-kZszbECjgrR8Xio2rn9ziQ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Enter the city name :")


@bot.message_handler(content_types=['text'])
def get_prayer_time(message):
    city = message.text.strip().title()
    date = datetime.datetime.utcfromtimestamp
    res = requests.get(f"https://api.aladhan.com/v1/timingsByAddress/date={date}?address={city}&method=99")

    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message,f""" Praying times in {city}🕌:
                     \n☪️{data['data']['date']['gregorian']['year']}-year,{data['data']['date']['gregorian']['weekday']['en']}🗓,{data['data']['date']['gregorian']['month']['number']}-{data['data']['date']['gregorian']['month']['en']}🗓
                     \n🏙Fajr: {data['data']['timings']['Fajr']}🕰
                     \n🌅Sunrise: {data['data']['timings']['Sunrise']}🕰
                     \n🏞Dhuhr: {data['data']['timings']['Dhuhr']}🕰
                     \n🌇Asr: {data['data']['timings']['Asr']}🕰
                     \n🌆Maghrib: {data['data']['timings']['Maghrib']}🕰
                     \n🌃Isha: {data['data']['timings']['Isha']}🕰
                     \n🌙Hijri date: {data['data']['date']['hijri']['date']}
                     \n☪️{data['data']['date']['hijri']['month']['en']}/{data['data']['date']['hijri']['month']['ar']}""")
    else:
        bot.reply_to(message,"Wrong name filled ! Try again")



bot.polling(non_stop=True)

