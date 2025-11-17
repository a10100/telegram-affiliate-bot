from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot afiliado está funcionando! Envie /link seguido do produto.")

async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Use assim: /link https://shopee.com/... ")
        return
    
    original = context.args[0]
    aff_link = original + "?aff_id=SEU_CÓDIGO_AQUI"
    await update.message.reply_text(f"Aqui está seu link afiliado:\n{aff_link}")

@app.route("/")
def home():
    return "Bot rodando!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
