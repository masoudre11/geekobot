import sys
import os
import flask
import telebot
import wikipedia
import urllib.request
import urllib.parse
import json
import textblob
import pyowm
import py_expression_eval
import youtubeapi
import goog
import poogle
import re
import random

from datetime import datetime
from atg.location import timezone
from string import Template

global bot

bot = telebot.TeleBot('240672059:AAGEAXv61hlBrb_nnrAaJcmE3m3Z6DvKucM') #TOKEN
app = flask.Flask(__name__)

bot.set_webhook('https://Shibbot-masoudre11.rhcloud.com/HOOK')

@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode()
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_messages([update.message])
        return 'ok'
    else:
        flask.abort(403)

@app.route('/')
def index():
    return 'Server is up and running'

@bot.message_handler(commands=['list', 'لیست'])
def send_welcome(message):
    bot.reply_to(message,
                 ("سلام، دستورات زیر موجود هستند:\n\n"
                  "/ویکی <متن>\n"
                  "/اپارات <متن>\n"
                  "/آپارات <متن>\n"
                  "/یوتیوب <متن>\n"
                  "/یو <متن>\n"
                  "/واژه <متن>\n"
                  "/ترجمه <متن>\n"
                  "/هوا <منطقه>\n"
                  "/حساب <متن>\n"
                  "/عکس <متن>\n"
                  "/گوگل <متن>\n"
                  "/ساعت <منطقه>\n"
                  "/لگد <اسم>"
                  "/حافظ\n"
                  "/بیت\n"
                  "/هشت\n"
                  "/8\n\n"
                  "/8ball\n"
                  "/translate <text>\n"
                  "/wiki <query>\n"
                  "/you <query>\n"
                  "/youtube <query>\n"
                  "/calc <eq>\n"
                  "/image <query>\n"
                  "/google <query>\n"
                  "/kick <person>\n"
                  "/time <location>\n"))
@bot.message_handler(commands=['help', 'راهنما'])
def send_welcome(message):
    bot.reply_to(message,
                 ("سلام، دستورات زیر موجود هستند:\n\n"
                  "/ویکی <متن>\n"
                  "جستجوی متن در ویکیپدیای فارسی\n"
                  "مثال: /ویکی سیاهچاله\n"
                  "/wiki <query>\n\n"
                  "جستجو در ویکیپدیای انگلیسی\n"
                  "مثال: \n/wiki blackhole\n\n"
                  "/اپارات <متن>\n"
                  "/آپارات <متن>\n"
                  "جستجوی ویدئو در آپارات\n"
                  "مثال: /آپارات موتسارت\n\n"
                  "/یوتیوب <متن>\n"
                  "/یو <متن>\n"
                  "/you <query>\n"
                  "/youtube <query>\n"
                  "جستجو ویدئو در یوتیوب\n"
                  "مثال: /یو Beethoven\n\n"
                  "/واژه <متن>\n"
                  "جستجو در واژه نامه ها\n"
                  "مثال: /واژه کیمیا\n\n"
                  "/ترجمه <متن>\n"
                  "ترجمه متن از هر زبانی به فارسی\n"
                  "مثال: /ترجمه Vivre sans aimer n’est pas proprement vivre.\n\n"
                  "/translate <text>\n"
                  "ترجمه از هر زبانی به زبان انگلیسی\n"
                  "مثال: \n/translate سلام دنیا\n\n"
                  "/هوا <منطقه>\n"
                  "آب و هوای مناطق\n"
                  "مثال: /هوا کرج\n"
                  "مثال: /هوا المان\n\n"
                  "/حساب <متن>\n/calc <eq>\n"
                  "محاسبات ریاضی\n"
                  "مثال: /حساب 2 + 2\n"
                  "/calc cos(45) * 3.14\n\n"
                  "/عکس <متن>\n/image <query>\n"
                  "جستجوی تصویر در گوگل\n"
                  "مثال: /عکس توت فرنگی\n\n"
                  "/گوگل <متن>\n/google <query>\n"
                  "جستجوی متن در گوگل\n"
                  "مثال: /گوگل طرز تهیه میرزاقاسمی\n\n"
                  "/حافظ\n"
                  "فال حافظ\n"
                  "مثال: /حافظ\n\n"
                  "/کیک\n/kick\n"
                  "لگد زدن به یک نفر!\n"
                  "مثال: /کیک @geekobot\n\n"
                  "/بیت\n"
                  "یک بیت شعر به صورت تصادفی\n"
                  "مثال: /بیت\n\n"
                  "/8\n/هشت\n/8ball\n"
                  "پیشگویی 8ball جادویی\n"
                  "مثال: /8\n\n"
                  "/ساعت <منطقه>\n/time <location>\n"
                  "ساعت مناطق مختلف\n"
                  "مثال: /ساعت ژاپن\n"
                  "/time tehran"))

@bot.message_handler(commands=['ویکی'])
def send_welcome(message):
    wikipedia.set_lang("fa")
    try:
        text      = ' '.join(message.text.split()[1:]).strip()
        response  = wikipedia.summary(text).strip()
        response += '\n\n\n' + wikipedia.page(text).url
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['wiki'])
def send_welcome(message):
    wikipedia.set_lang("en")
    try:
        text      = ' '.join(message.text.split()[1:]).strip()
        response  = wikipedia.summary(text).strip()
        response += '\n\n\n' + wikipedia.page(text).url
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['اپارات', 'آپارات'])
def send_welcome(message):
    try:
        text      = ' '.join(message.text.split()[1:]).strip()
        request   = 'http://www.aparat.com/etc/api/videoBySearch/text/'+urllib.parse.quote_plus(text)+'/perpage/1000'
        search    = urllib.request.urlopen(request).readall().decode()
        results   = json.loads(search)
        if results['videobysearch']:
            choice   = max(results['videobysearch'], key = lambda r: r['visit_cnt'])
            response = 'http://aparat.ir/v/'+choice['uid']
        else:
            response = 'چیزی پیدا نشد'
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['you', 'یو', 'youtube', 'یوتیوب'])
def send_welcome(message):
    try:
        text     = ' '.join(message.text.split()[1:]).strip()
        youtube  = youtubeapi.YoutubeAPI({'key': 'AIzaSyDwwXm3B0JI460jevFEkC-o0Fngfe3BG2o'})
        videos   = youtube.search_videos(text)
        response = 'http://youtube.com/watch?v=' + videos[0]['id']['videoId']
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['واژه'])
def send_welcome(message):
    try:
        text      = ' '.join(message.text.split()[1:]).strip()
        request   = 'http://api.vajehyab.com/v2/public/?q='+urllib.parse.quote_plus(text)+'&developer=geekobot'
        query     = urllib.request.urlopen(request).readall().decode()
        results   = json.loads(query[1:])
        if results['search']['code'] == 200:
            data      = results['data']
            response  = data['title']
            response += data['pronunciation'] and '('+data['pronunciation']+')' or ''
            response += '\n\n' + data['text']
        else:
            response = results['error']['message']
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['ترجمه'])
def send_welcome(message):
    try:
        text     = ' '.join(message.text.split()[1:]).strip()
        blob     = textblob.TextBlob(text)
        response = blob.translate(to='fa').raw
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['translate'])
def send_welcome(message):
    try:
        text     = ' '.join(message.text.split()[1:]).strip()
        blob     = textblob.TextBlob(text)
        response = blob.translate(to='en').raw
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['هوا'])
def send_welcome(message):
    try:
        text     = ' '.join(message.text.split()[1:]).strip()
        owm      = pyowm.OWM('e666a0fcb06cd4818b3c99e076c26fae')
        w        = owm.weather_at_place(text).get_weather()
        temp     = w.get_temperature('celsius')
        response = 'دمای %s حداقل %s حداکثر %s، سرعت باد %s، رطوبت %s'%(
                        text, temp['temp_min'], temp['temp_max'], w.get_wind()['speed'], w.get_humidity())
        response += '، وضعیت ابر: %s، باران: %s، برف: %s. فشار هوا: %s'%(
                        str(w.get_clouds())+'%', w.get_rain() and 'بله' or 'نه', w.get_snow() and 'بله' or 'نه', int(w.get_pressure()['press']))

        forecast = owm.daily_forecast(text)
        tomorrow = pyowm.timeutils.tomorrow()
        w        = forecast.get_weather_at(tomorrow)
        temp     = w.get_temperature('celsius')
        response += '\n\nپیشبینی روز آینده:\n'
        response += 'دمای %s حداقل %s حداکثر %s، سرعت باد %s، رطوبت %s'%(
                        text, temp['min'], temp['max'], w.get_wind()['speed'], w.get_humidity())
        response += '، وضعیت ابر: %s، باران: %s، برف: %s. فشار هوا: %s'%(
                        str(w.get_clouds())+'%', w.get_rain() and 'بله' or 'نه', w.get_snow() and 'بله' or 'نه', int(w.get_pressure()['press']))
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['حساب', 'calc'])
def send_welcome(message):
    try:
        parser   = py_expression_eval.Parser()
        text     = ' '.join(message.text.split()[1:]).strip()
        response = str(parser.parse(text).evaluate({}))
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['image', 'عکس'])
def send_welcome(message):
    try:
        text     = ' '.join(message.text.split()[1:]).strip()
        images   = goog.get_images(text)
        agent    = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        headers  = {'User-Agent':agent,}
        response = images[0]
        for img in images:
            try:
                image_request = urllib.request.Request(img, None, headers)
                image_remote  = urllib.request.urlopen(image_request)
                if image_remote.headers['Content-Type'].split(';')[0].lower().split('/')[0] == 'image':
                    response = img
                    break
            except Exception as e:
                response = str(e)
                continue
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['google', 'گوگل'])
def send_welcome(message):
    try:
        text     = ' '.join(message.text.split()[1:]).strip()
        results  = goog.get_search(text)
        response = ''
        for r in results[:4]:
            response += r[0] + '\n'
            response += r[1] + '\n'
            response += r[2] + '\n\n'
        response = response.strip()
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['حافظ'])
def send_welcome(message):
    try:
        url      = 'http://pichak.net/hafez/fal.php'
        agent    = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
        headers  = {'User-Agent':agent,}
        request  = urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request).readall().decode()
        response = response[response.find('<b>تعبیر: </b>')+14:]
        response = response[:response.find('<br>')]
        response = response.replace('\ufeff', '').strip()
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['بیت'])
def send_welcome(message):
    try:
        url      = 'http://c.ganjoor.net/beyt.php'
        results = urllib.request.urlopen(url).readall().decode()
        shaer   = re.search('<a href="[^"]*">([^<]*)</a>', results).group(1)
        m1      = re.search('<div class="ganjoor-m1">([^<]*)</div>', results).group(1)
        m2      = re.search('<div class="ganjoor-m2">([^<]*)</div>', results).group(1)
        response = m1 + '\n' + m2 + '\n\n' + shaer
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['ساعت', 'time'])
def send_welcome(message):
    try:
        text     = ' '.join(message.text.split()[1:]).strip()
        response = datetime.now(timezone(text)).strftime('%H:%M')
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['8', '8ball', 'هشت'])
def send_welcome(message):
    try:
        options  = ['نشونه ها میگن که قطعیه',
                    'بله',
                    'مبهم جواب بده، دوباره امتحان کن',
                    'بدون شک',
                    'منابع من میگن نه',
                    'اینطوری که من میبینم، آره',
                    'میتونی بهش اعتماد کنی',
                    'تمرکز کن و دوباره بپرس',
                    'به نظر زیاد خوب نمیاد',
                    'موضوع خیلی واضحه، بهش شک نکن',
                    'بهتره الان بهت نگم',
                    'خیلی شک دارم',
                    'آره، حتما.',
                    'این موضوع مسلمه',
                    'الان نمیتونم پیش بینی کنم',
                    'ممکنه خوب باشه',
                    'بعدا ازم بپرس',
                    'جواب من نه هست',
                    'به نظر که خوب میاد',
                    'روش حساب باز نکن']
        response = random.choice(options)
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

@bot.message_handler(commands=['لگد', 'kick'])
def send_welcome(message):
    try:
        kicker   = '\u061C'+message.from_user.first_name
        kickee   = '\u061C'+' '.join(message.text.split()[1:]).strip()
        if len(kickee) == 1:
            raise Exception('کسی رو برای لگد مشخص نکردید')
        strings  = [Template('یه جادوی خیلی قوی $kickee را کشت'),
                    Template('$kickee با یه لگد محکم به ملکوت اعلی پیوست'),
                    Template('$kicker $kickee را از بالای یک ساختمان به پایین پرت کرد'),
                    Template('$kickee مرد! همش تقصیره $kicker بود!'),
                    Template('$kickee مرد و حالا تبدیل به یه روح شده'),
                    Template('$kickee داشت از دست $kicker فرار می کرد که محکم خورد به یه کاکتوس'),
                    Template('$kickee از گوشه دنیا افتاد پایین'),
                    Template('$kickee یه نارنجکو قورت داد!'),
                    Template('$kickee از گرسنکی مرد'),
                    Template('$kickee منفجر شد'),
                    Template('$kickee تبدیل به یه سیب زمینی شد'),
                    Template('شست $kickee رفت تو چشمش'),
                    Template('$kicker درسته $kickee رو قورت داد'),
                    Template('$kicker $kickee رو از صحنه روزگار محو کرد'),
                    Template('$kicker با دینامیت $kickee رو منهدم کرد'),
                    Template('$kickee توسط هیولای زیر تختش خورده شد'),
                    Template('$kickee توسط $kicker نابود شد'),
                    Template('$kickee توسط $kicker نابود شد'),
                    Template('$kickee محکم به زمین خورد'),
                    Template('$kickee افتاد رو شمشیر خودش'),
                    Template('$kickee امشب با ماهیا میخوابه'),
                    Template('از $kickee هیچی به جز استخوناش باقی نمونده'),
                    Template('رعد و برق $kickee رو از وسط دو تیکه کرد'),
                    Template('$kicker $kickee رو بمبارون کرد'),
                    Template('$kicker $kickee رو با اره دو تیکه کرد'),
                    Template('$kickee به صورت عمودی به دو تیکه تقسیم شد'),
                    Template('$kickee مثه سیب زمینی خلال شد'),
                    Template('$kicker شام $kickee سرخ شده میخوره'),
                    Template('$kicker به $kickee شلیک کرد'),
                    Template('$kicker $kickee رو با ذره بین سوزوند'),
                    Template('$kickee وقتی که داشت از دست $kicker فرار می کرد غرق شد'),
                    Template('$kickee از یه نردبون افتاد پایین'),
                    Template('یه نهنگ بزرگ افتاد روی $kickee و لهش کرد'),
                    Template('یه هواپیما روی سر $kickee سقوط کرد'),
                    Template('یه اتوبوس از روی $kickee رد شد'),
                    Template('حتی جنازه $kickee رو هم پیدا نکردن'),
                    Template('مورچه ها $kickee رو خوردن'),
                    Template('$kickee ترک برداشت'),
                    Template('$kickee از شدت ضربه بیهوش شد'),
                    Template('$kicker موهای $kickee رو کند'),]
        response = random.choice(strings).safe_substitute(kicker=kicker, kickee=kickee)
    except Exception as e:
        response = str(e)
    bot.reply_to(message, response)

# Handle all other messages
#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def echo_message(message):
#    bot.reply_to(message, message.text)
