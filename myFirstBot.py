import requests as requests

url = "https://api.telegram.org/MY_BOT_TOKEN_GOES_HERE/"

#create func that get id

def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id

#create  func that get message text

def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text

#create  func that get username

def get_username(update):
    username = update["message"]["chat"]["first_name"]
    return username


#create func that get last update

def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    if len(result) == 100:
        last_update(req + "getUpdates?offset=" + str(result[len(result)- 1]["update_id"]))
    total_updates = len(result) - 1
    print(len(result))
    return result[total_updates]    #get last record message update

#create func that send message to user

def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response

#create main func for navigate or reply message back

def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if  get_message_text(update).lower() == "/start" or get_message_text(update).lower() == "hi" or  get_message_text(update).lower() == "hello":
                send_message(get_chat_id(update), 'Hello ' + get_username(update) + '! Welcome to my first bot :) Type "play" to start!')
            elif get_message_text(update).lower() == "play":
                send_message(get_chat_id(update), 'This is just a demo silly... Try something else.')
            else:
                send_message(get_chat_id(update), 'Sorry. I can\'t understand you. Actually, i\'m a little dumb. Could you please draw it for me?')
            update_id += 1

#call func to make it reply
main()
