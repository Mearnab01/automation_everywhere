from telegram import Update
from telegram.ext import Application , CommandHandler , MessageHandler, filters , ContextTypes

TOKEN = "" #telegram token
BOT_USENAME = "@bias_bot_ArthGenerated"

#commands
async def start_command(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! I am BIAS.. How Can i assist You??")

async def help_command(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
    Here are the available commands:
    /start - Start the bot and receive a welcome message.
    /help - View this help message.
    /custom - Execute a custom command.
    """
    )

async def custom_command(update: Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command. You can replace this text with your custom functionality.")

#basic message
def handle_response(text:str):
    processed:str = text.lower()

    if 'hello' in processed:
        return 'Hey, there!'
    elif 'how are you' in processed:
        return 'I am just a computer program, but I am here to assist you!'
    elif 'thank you' in processed:
        return 'You are welcome!'
    elif 'bye' in processed:
        return 'Goodbye! If you have more questions, feel free to ask.'
    else:
        return 'I am not sure how to respond to that. Please ask another question or type a command.'

# Example usages:
#response1 = handle_response('Hello')
#print(response1)

#handling message
async def handle_message(update :Update, context: ContextTypes.DEFAULT_TYPE ):
    message_type:str = update.message.chat.type
    text: str = update.message.text

    print(f"User {update.message.chat.id} in {message_type} : {text}")

    if message_type == 'group':
        if BOT_USENAME in text:
            new_text:str = text.replace(BOT_USENAME,'').strip()
            response:str = handle_response(new_text)
        return 
    else:
        response:str = handle_response(text)

    print("Bot: ",response)
    await update.message.reply_text(response)

#error
async def error_handler(update: Update,context:ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} casued error {context.error}")

if __name__ == "__main__":
    print("Starting...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error_handler)

    print("polling..")
    app.run_polling(poll_interval=3)