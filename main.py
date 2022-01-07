import asyncio
from pytgcalls import idle
from driver.amort import call_py, bot

async def mulai_bot():
    print("[amort]: STARTING BOT CLIENT")
    await bot.start()
    print("[amort]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[amort]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())