from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import hi_command, time_command, help_command, sum_command

app = ApplicationBuilder().token("5465515970:AAH4_N-42H07fzGkkVFWHjY8wQoOIPU8wI4").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()