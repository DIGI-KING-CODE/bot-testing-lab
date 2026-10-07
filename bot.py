import os
import logging
from tests import run_all_tests
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT TESTING LAB\n\n"
        "Available commands:\n"
        "/help - Show commands\n"
        "/status - Check runner status\n"
        "/run - Run basic self-test"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start bot\n"
        "/help - Show help\n"
        "/status - Check status\n"
        "/run - Run basic self-test"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 Test Runner is online.\n"
        "Automated target-bot tests are not configured yet."
    )


async def run_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    report = run_all_tests()
    await update.message.reply_text(report)
    
    report = "🧪 SELF-TEST REPORT\n\n"
    for name, passed in checks.items():
        report += f"{'✅ PASS' if passed else '❌ FAIL'} — {name}\n"
    await update.message.reply_text(report)


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("run", run_test))
    app.run_polling()


if __name__ == "__main__":
    main()

