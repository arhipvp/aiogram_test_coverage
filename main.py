import asyncio
import logging

import my_bot


async def main() -> None:
    await my_bot.dp.start_polling(my_bot.bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())