from currency_converter import CurrencyConverter
from telegram.ext import ApplicationBuilder, CommandHandler
from prompt import get_values_from_input
from dotenv import load_dotenv
import os
import logging


def converter(input_json):
    try:
        amount, from_currency, to_currency = (
            input_json["amount"],
            input_json["source_currency"],
            input_json["destination_currency"],
        )
        c = CurrencyConverter()
        return c.convert(amount, from_currency.upper(), to_currency.upper())
    except ValueError:
        return "Unsupported Currency"
    except KeyError:
        logging.error("Malformed Query. e.g. query \n/convert 3000 inr to usd")


async def convert_handler(update, context):
    input_json = get_values_from_input(" ".join(context.args))
    if "error" in input_json:
        result="Invalid/Malformed Query. e.g. query \n/convert 3000 inr to usd"
    else:
        result = converter(input_json)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)


if __name__ == "__main__":
    load_dotenv()

    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    convert_handler = CommandHandler("convert", convert_handler)
    app.add_handler(convert_handler)

    app.run_polling()
