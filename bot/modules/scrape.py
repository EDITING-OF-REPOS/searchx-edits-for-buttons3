from telegram.ext import CommandHandler
from telegram import InlineKeyboardMarkup
from bot import AUTHORIZED_CHATS, dispatcher
from bot.helper.ext_utils.bot_utils import new_thread
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage, sendMarkup
from bot.helper.telegram_helper import button_builder
from bot.helper.ext_utils.parser import get_gp_link

@new_thread
def scrape_gp(update, context):
    buttons = button_builder.ButtonMaker()
    buttons.buildbutton("❤️‍🔥 JNS BOTS ❤️‍🔥", "https://t.me/JNS_BOTS")
    buttons.buildbutton("🧲JNS LEECHS🧲", "https://t.me/JNS_MIRROR")
    reply_markup = InlineKeyboardMarkup(buttons.build_menu(1))
    try:
       query = update.message.text.split()[1]
    except:
       sendMarkup('<b>send a GPLinks along with this command 👀\n\n ❗️reply to the link wont wokrs❗️</b>\n👉🏻 command GpLink', context.bot, update, reply_markup)
       return
 
    if not query.startswith("https://gplinks") or query.startswith("gplinks"):
       sendMessage('<b>Sorry 🤐 , <i>scrape only for GPLinks URLs. \nYou can use clone for GDrive, GdTot, AppDrive URLs</i> 🤠</b>', context.bot, update)
       return

    m = sendMessage('<b>🚀🚀 Please wait a sec...\nDont give another task 🙅 </b>', context.bot, update)
    link = get_gp_link(query)
    deleteMessage(context.bot, m)
    if not link:      
       sendMessage("Something went wrong\nTry again later..🥺 ", context.bot, update)
    else:
       buttons = button_builder.ButtonMaker()
       buttons.buildbutton("✨ BYPASSED LINK ✨", link)
       buttons.buildbutton("❤️‍🔥 JNS BOTS ❤️‍🔥", "https://t.me/JNS_BOTS")
       reply_markup = InlineKeyboardMarkup(buttons.build_menu(1))
       sendMarkup(f"<b>Thank you for using me 💫 \n\nHere is your direct link</b>\n<code>{link}</code>\n\n", context.bot, update, reply_markup)

gplink_handler = CommandHandler("scrape", scrape_gp,
                               filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(gplink_handler)
