import vk_api
import config

def messagesFormating(messages):

	format_messages = list()

	for key in messages.keys():
		temp = messages[key]
		temp['from_id'] = key
		format_messages.append(temp)

	return format_messages


def getUnreadMessages(session):

	unread_messages = dict()
	messages = session.messages.get(count = 20)

	for message in messages['items']:
		if message['read_state'] == 0:
			session.messages.markAsRead(message_ids = message['id'])
			users = session.users.get(user_ids = message['user_id'])
			for user in users:
				if user['id'] in unread_messages.keys():
					unread_messages[user['id']]['message_text'] += '\n' + '\n' + message['body']
				else:
					temp = dict()
					temp['from_fname'] = user['first_name']
					temp['from_lname'] = user['last_name']
					temp['message_text'] = message['body']
					unread_messages[user['id']] = temp

	return messagesFormating(unread_messages)


def main(): 
    vk_session = vk_api.VkApi(config.vk_login, config.vk_password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    return getUnreadMessages(vk)
