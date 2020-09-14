import telepot
token= '1303246656:AAHy_TlQbO47A3BebzyfRiCxokF_tXcopy8'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
content_type, chat_ty DCpe, chat_id = telepot.glance(msg)
print(content_type, chat_type, chat_id)

if content_type == 'text':
bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
