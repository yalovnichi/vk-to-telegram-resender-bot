import config
import telebot
import time
from vk_messages_control import get_messages

bot = telebot.TeleBot(config.token)
_main_flag = None

@bot.message_handler(commands=['start'])
def get_messages_from_vk(message):
	while True:
		mfv = get_messages()
		if mfv:
			for point in mfv:
				address = 'from:	vk\n'
				sender = 'by : ' + point.from_fname + ' ' + point.from_lname + '\n'
				msg = address + sender + point.message_text
				bot.send_message(message.chat.id, msg)
				print(msg)
				time.sleep(0.5)
			time.sleep(3)
		else:
			time.sleep(3) 
			continue
	

@bot.message_handler(commands = ['close']) 
def GoodbayMessage(message):
	bot.send_message(message.chat.id,'Goodbay, Stas!')
	_main_flag = False   

@bot.message_handler(commands = ['send_message'])
def 

if __name__ == '__main__':
	bot.polling(none_stop=True)