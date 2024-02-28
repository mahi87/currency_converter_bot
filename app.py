from currency_converter import CurrencyConverter
from telegram.ext import ApplicationBuilder, CommandHandler


def converter(input_arr):
    try:
        amount, from_currency, to_currency = input_arr[0], input_arr[1], input_arr[3]
        c = CurrencyConverter()
        return c.convert(amount, from_currency.upper(), to_currency.upper())
    except ValueError:
        return "Unsupported Currency"
    except IndexError:
        return "Malformed Query. e.g. query \n/convert 3000 inr to usd"


async def convert_handler(update, context):
    result = converter(context.args)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)


if __name__ == "__main__":
    app = (
        ApplicationBuilder()
        .token("7163740926:AAHFPHZpWQw75684BxRtHjQs5DPruXMxTM8")
        .build()
    )
    convert_handler = CommandHandler("convert", convert_handler)
    app.add_handler(convert_handler)

    app.run_polling()
