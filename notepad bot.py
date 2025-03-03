from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import requests
import asyncio

# Function to fetch a joke
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    return "I couldn't fetch a joke, try again later!"

# Command function for the bot
async def joke(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(get_joke())

def main():
    TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your actual bot token
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("joke", joke))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
