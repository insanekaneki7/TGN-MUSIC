import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        ***𝗛𝗘𝗬𝗬...𝗕𝗔𝗕𝗬🥀👀😎***

***𝗜 𝗮𝗺 𝗮𝗻...
⛩️𝗜𝗡𝗦𝗔𝗡𝗘 𝗖𝗔𝗧𝗖𝗛𝗘𝗥 𝗕𝗢𝗧⛩️
𝗔𝗱𝗱 𝗠𝗲 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗜 𝘄𝗶𝗹𝗹 𝘀𝗲𝗻𝗱 𝗥𝗮𝗻𝗱𝗼𝗺 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀𝗔𝗳𝘁𝗲𝗿.. 𝗲𝘃𝗲𝗿𝘆 𝟮𝟱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗶𝗻 𝗚𝗿𝗼𝘂𝗽... 𝗨𝘀𝗲 /guess 𝘁𝗼.. 𝗖𝗼𝗹𝗹𝗲𝗰𝘁 𝘁𝗵𝗮𝘁 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻.. 𝗮𝗻𝗱 𝘀𝗲𝗲 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻 𝗯𝘆 𝘂𝘀𝗶𝗻𝗴 /harem... 𝗦𝗼 𝗮𝗱𝗱 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽𝘀 𝗮𝗻𝗱 𝗖𝗼𝗹𝗹𝗲𝗰𝘁 𝗬𝗼𝘂𝗿 𝗵𝗮𝗿𝗲𝗺***
        """
        
        keyboard = [
            [InlineKeyboardButton("😎𝙆𝙄𝘿𝙉𝘼𝙋 𝙈𝙀😎", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("⛩️𝙎𝙐𝙋𝙋𝙊𝙍𝙏⛩️", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("🎁𝙐𝙋𝘿𝘼𝙏𝙀🎁", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("⚡𝘼𝘽𝙄𝙇𝙄𝙏𝙄𝙀𝙎⚡", callback_data='help')],
            [InlineKeyboardButton("🥀𝙊𝙒𝙉𝙀𝙍🥀", url=f'https://t.me/abtkaneki')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("😎𝙆𝙄𝘿𝙉𝘼𝙋 𝙈𝙀😎", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("⛩️𝙎𝙐𝙋𝙋𝙊𝙍𝙏⛩️", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("🎁𝙐𝙋𝘿𝘼𝙏𝙀🎁", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("⚡𝘼𝘽𝙄𝙇𝙄𝙏𝙄𝙀𝙎⚡", callback_data='help')],
            [InlineKeyboardButton("🥀𝙊𝙒𝙉𝙀𝙍🥀", url=f'https://t.me/abtkaneki')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="🎴Alive!?... \n connect to me in PM For more information ",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***Help Section:***
    
***/guess: To Guess character (only works in group)***
***/fav: Add Your fav***
***/trade : To trade Characters***
***/gift: Give any Character from Your Collection to another user.. (only works in groups)***
***/collection: To see Your Collection***
***/topgroups : See Top Groups.. Ppl Guesses Most in that Groups***
***/top: Too See Top Users***
***/ctop : Your ChatTop***
***/changetime: Change Character appear time (only works in Groups)***
   """
        help_keyboard = [[InlineKeyboardButton("⤾ Bᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        ***𝗛𝗘𝗬𝗬...𝗕𝗔𝗕𝗬🥀👀😎*** ✨

***𝗜 𝗮𝗺 𝗮𝗻...
⛩️𝗜𝗡𝗦𝗔𝗡𝗘 𝗖𝗔𝗧𝗖𝗛𝗘𝗥 𝗕𝗢𝗧⛩️
𝗔𝗱𝗱 𝗠𝗲 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗔𝗻𝗱 𝗜 𝘄𝗶𝗹𝗹 𝘀𝗲𝗻𝗱 𝗥𝗮𝗻𝗱𝗼𝗺 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀𝗔𝗳𝘁𝗲𝗿.. 𝗲𝘃𝗲𝗿𝘆 𝟮𝟱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗶𝗻 𝗚𝗿𝗼𝘂𝗽... 𝗨𝘀𝗲 /guess 𝘁𝗼.. 𝗖𝗼𝗹𝗹𝗲𝗰𝘁 𝘁𝗵𝗮𝘁 𝗖𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿𝘀 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻.. 𝗮𝗻𝗱 𝘀𝗲𝗲 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻 𝗯𝘆 𝘂𝘀𝗶𝗻𝗴 /harem... 𝗦𝗼 𝗮𝗱𝗱 𝗶𝗻 𝗬𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽𝘀 𝗮𝗻𝗱 𝗖𝗼𝗹𝗹𝗲𝗰𝘁 𝗬𝗼𝘂𝗿 𝗵𝗮𝗿𝗲𝗺***
        """

        
        keyboard = [
            [InlineKeyboardButton("😎𝙆𝙄𝘿𝙉𝘼𝙋 𝙈𝙀😎", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("⛩️𝙎𝙐𝙋𝙋𝙊𝙍𝙏⛩️", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("🎁𝙐𝙋𝘿𝘼𝙏𝙀🎁", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("⚡𝘼𝘽𝙄𝙇𝙄𝙏𝙄𝙀𝙎⚡", callback_data='help')],
            [InlineKeyboardButton("🥀𝙊𝙒𝙉𝙀𝙍 🥀", url=f'https://t.me/abtkaneki')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)