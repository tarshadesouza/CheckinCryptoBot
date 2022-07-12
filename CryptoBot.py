from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# Updater: This will contain the API key we got from BotFather to specify in which bot we are adding functionalities to using our python code.
# Update: This will invoke every time a bot receives an update i.e. message or command and will send the user a message.
# CallbackContext: We will not use its functionality directly in our code but when we will be adding the dispatcher it is required (and it will work internally)
# CommandHandler: This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc.
# MessageHandler: This Handler class is used to handle any normal message sent by the user to the bot,
# FIlters: This will filter normal text, commands, images, etc from a sent message.


    
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to Checkin Crypto Bot it's used to allow easy access to check your funds or buy some new tokens.")
    
def help(update: Update, context: CallbackContext):
	update.message.reply_text("Your Message")

 
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
    
def main():
    updater = Updater("5331460918:AAGgv-6BLr5TOSqQxxO1itSjNlqco0xVQy4",
                  use_context=True)
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    
    dp.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
    dp.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
# Filters out unknown messages.
    dp.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# Start the Bot   
    updater.start_polling()
    updater.idle()
