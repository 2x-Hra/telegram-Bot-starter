from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, \
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent

'''
    it's another example of Inline use of telegram bot ,
    after writing ur bot username instert space and enter whatever you want 
    then send it .
'''
def IKM(data):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, cbd)] for text, cbd in data])


app = Client('mybot')
data = []


@app.on_callback_query()
def handle_callback_query(bot: Client, query: CallbackQuery):
    user_id = query.from_user.id
    for rec in data:
        if rec[0] == query.inline_message_id:
            if user_id in rec[1]:
                rec[1].remove(user_id)
            else:
                rec[1].append(user_id)
            count = len(rec[1])
            break
    else:
        data.append([query.inline_message_id, [user_id]])
        count = 1
    if query.data == 'like':
        bot.edit_inline_reply_markup(query.inline_message_id, IKM([(f'❤ ({count})️', 'like')]))


@app.on_inline_query()
def handle_inline_query(bot: app, query: InlineQuery):
    if not query.query:
        return
    results = [InlineQueryResultArticle(f'Like version of {query.query}', InputTextMessageContent(query.query),
                                        reply_markup=IKM([('❤ (0)️', 'like')]))]
    bot.answer_inline_query(query.id, results)


app.run()