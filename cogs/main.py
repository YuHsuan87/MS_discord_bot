import discord
import os

from datetime import datetime, timezone, timedelta
from discord.ext import commands

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot    

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        if "udong" in message.content:
            # 設定為 +8 時區, 取得現在時間、指定時區、轉為 ISO 格式
            tz = datetime.now(timezone(timedelta(hours=+8))).isoformat(timespec="seconds")[:-6]
            await message.channel.send(f"udong! wake up! {tz}.")

        if "claudi" in message.content:
            await message.channel.send("Will you graduate? Good luck for your oral presentation.")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))