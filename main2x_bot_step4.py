from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, \
    InlineQueryResultArticle, InputTextMessageContent

'''
    this code is an example of Inline action for telegram bot , 
    if u wanna test this you have to type @yourbotusername and then space 
    it will show a inline call then u press it and so on
'''

def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])


app = Client('mybot')


@app.on_callback_query()
def handle_callback_query(bot: Client, query: CallbackQuery):
    if query.data == 'start':
        bot.edit_inline_text(query.inline_message_id, 'توضیحات بازی', reply_markup=IKM([('پایان', 'end')]))
    elif query.data == 'end':
        bot.edit_inline_text(query.inline_message_id, 'بازی تمام شد!!')


@app.on_inline_query()
def handle_inline_query(bot: Client, query: InlineQuery):
    results = [InlineQueryResultArticle('شروع بازی جدید', InputTextMessageContent('متن بلند'),
                                        reply_markup=IKM([('قبول بازی!', 'start')]))]
    bot.answer_inline_query(query.id, results)


app.run()
