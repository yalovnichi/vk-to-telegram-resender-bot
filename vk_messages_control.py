import vk_api
import config

class Message:
	def __init__(self,from_id,from_fname,from_lname,message_text):
		self.from_id = from_id
		self.from_fname = from_fname
		self.from_lname = from_lname
		self.message_text = message_text


def messages_formatting(messages):

	format_messages = list()

	for key in messages.keys():
		temp = Message(key, messages[key]['from_fname'], messages[key]['from_lname'], messages[key]['message_text'])	
		format_messages.append(temp)

	return format_messages


def get_unread_messages(session):

	unread_messages = dict()
	messages = session.messages.get(count = 20)

	for message in messages['items']:
		if message['read_state'] == 0:
			#session.messages.markAsRead(message_ids = message['id'])
			users = session.users.get(user_ids = message['user_id'])
			for user in users:
				if user['id'] in unread_messages.keys():
					unread_messages[user['id']]['message_text'] += '\n\n' + message['body']
				else:
					temp = dict()
					temp['from_fname'] = user['first_name']
					temp['from_lname'] = user['last_name']
					temp['message_text'] = message['body']
					unread_messages[user['id']] = temp

	return messages_formatting(unread_messages)


def get_messages(): 
    vk_session = vk_api.VkApi(config.vk_login, config.vk_password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    return get_unread_messages(vk)



