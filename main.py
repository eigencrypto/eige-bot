from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="7727152018:AAGP80S_LdburlQye1DwhMuRjtxpyiE87_U")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="CLAIM AIRDROP",
            web_app=types.WebAppInfo(url="https://eigecrypto.world")
        )
    )

    await message.answer(
        "Welcome to EIGE Airdrop!\n\n"
        "Claim your early access rewards and explore the future of Ethereum-based projects.\n\n"
        "Click the button below to get started.",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
