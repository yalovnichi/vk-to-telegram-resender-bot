import config
import telebot
import time
import vk_messages_control as vmk

bot = telebot.TeleBot(config.token)



@bot.message_handler(commands=['vk'])
def sendMessagesFromVk(message):
	while True:
		mfv = vmk.main()
		print(mfv)
		for point in mfv:
			msg = 'from: ' + point['from_fname'] + ' ' + point['from_lname'] + '\n' + point['message_text']
			bot.send_message(message.chat.id, msg)
			time.sleep(0.5)
		time.sleep(5)
@bot.message_handler(commands = ['close']) 
def GoodbayMessage(message):
	bot.send_message(message.chat.id,'Goodbay, Stas!')   


if __name__ == '__main__':
	bot.polling(none_stop=True)