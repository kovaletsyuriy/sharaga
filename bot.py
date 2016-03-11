# -*- coding: utf-8 -*-
import config
import telebot
import time
from pyquery import PyQuery
html = open("index.html", 'r').read()

def listener(messages):
    for oneMes in messages:
    	string = ""
        if oneMes.content_type == 'text':
			jQuery = PyQuery(html)
			qu = oneMes.text.encode('utf-8')
			for x in jQuery("td"):
				result = jQuery(x).children().eq(0).text().encode('utf-8').strip()
				if result == qu:
					for i in xrange(1,5):
						string = string + jQuery(x).children().eq(i).text().strip() + "\n"
					bot.send_message(oneMes.chat.id, string)


if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)
     while True:
         time.sleep(200)