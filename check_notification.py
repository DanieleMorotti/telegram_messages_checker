from telethon import TelegramClient, events
import logging, playsound, re

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = api_id_number
API_HASH = "your api hash"

# The first parameter is the .session file name (absolute paths allowed)
client = TelegramClient("session_file", API_ID, API_HASH)

#write the words you want to check in messages (for example: ["urgent","important"])
words_to_check = [""]

def find_words(text):
    global words_to_check
    query = ""
    for word in words_to_check:
        query += fr'\b{word}.?\b|'
    query = query[:-1]
    return re.search(query,text,flags=re.I | re.M)
    
    
chats = [''] #example chats = ["first_chat_name","second_chat_name"]
#check if the last 3 messages in the chats inserted below have the chosen words
async def check_old(chats):
    data = await client(functions.messages.GetPeerDialogsRequest(peers=chats))
    #find chats with unread messages between @chats
    to_check = [data.chats[i].title for i,chat in enumerate(data.dialogs) if chat.unread_count > 0]
    for name in to_check:
        messages = await client.get_messages(name, limit=3)
        for mes in messages:
            #the selected regex find if in the message there are word1 or word2 as single words(not in compound words) in case unsensitive mode
            is_found = find_words(mes.message)
            if is_found is not None:
                playsound.playsound('path_to_file', True)
                
with client:
    client.loop.run_until_complete(check_old(chats))
    

print("I'm waiting for new messages ...")
@client.on(events.NewMessage)
async def new_message_listener(event):
    txt = event.raw_text
    is_found = find_words(txt)
    if is_found is not None: 
        playsound.playsound('path_to_file', True)
    else:
        print(txt)
       
client.start()
client.run_until_disconnected()