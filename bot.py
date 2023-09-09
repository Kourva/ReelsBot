#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

# Instagram reels downloader bot by Kourva
# Github: https://github.com/kourva/ReelsBot

# Resources
import telebot
import datetime

# Initializing Bot
with open("Token.env", "r") as secret:
    try:
        bot = telebot.TeleBot(secret.read().split("=")[1].strip())
    except:
        print("It seems that Token is invalid. edit Token.env")

# Start command handler
@bot.message_handler(commands=["start"])
def start_command(message):

    # Get user's first name and chat ID
    cid = message.chat.id
    ufn = message.from_user.first_name

    # Send greetings to user
    bot.send_chat_action(chat_id=cid, action="typing")
    bot.reply_to(
        message=message, 
        text=f"Hi {ufn}! Send URL to me"
    )

# Handling Instagram links
@bot.message_handler(func=lambda message: "www.instagram.com" in message.text)
def url_handler(message: callable) -> None:

    # Get chat id
    cid = message.chat.id
    bot_id = bot.get_me().id

    try:
        # Send Instagram post to user
        bot.send_chat_action(chat_id=cid, action="upload_document")
        bot.send_document(
            chat_id=cid,
            document=message.text.replace("instagram.com", "DDinstagram.com"),
            reply_to_message_id=message.message_id,
            caption=f"Sent in {datetime.datetime.now().strftime('%d %h %Y at %H:%M:%S')}\n[Via](tg://user?id={bot_id})",
            reply_markup=telebot.util.quick_markup({"Open In Instagram": {"url": message.text}}),
            parse_mode="MarkdownV2"
        )
        
    except Exception as ex:
        # Send message to user
        bot.send_chat_action(chat_id=cid, action="typing")
        bot.reply_to(
            message=message, 
            text="Could not get video!"
        )
        
        # Print error message
        print(f"Error Due to {ex}")


# Start the bot
if __name__ == "__main__":
    try:
        bot.infinity_polling(skip_pending=False, none_stop=True)
    except Exception as ex:
        print(f"Error due to {ex}")