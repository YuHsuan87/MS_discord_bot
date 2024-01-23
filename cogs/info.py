import discord
import os

from discord.ext import commands

# 定義名為 Info 的 Cog
class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # send_picture
    def send_picture(self, pic_name):
        pic_path = os.path.join("cogs", "pic", pic_name)
        pic = discord.File(pic_path)
        return pic
    
    # 前綴指令
    # skill points
    @commands.command()
    async def 破風(self, ctx:commands.Context):
        await ctx.send("https://forum.gamer.com.tw/C.php?bsn=7650&snA=1016324&tnum=190")
        await ctx.send(file = self.send_picture("wind_archer.png"))

    @commands.command()
    async def 阿戴爾(self, ctx:commands.Context):
        await ctx.send(file = self.send_picture("adale.png"))

    @commands.command()
    async def 火毒(self, ctx:commands.Context):
        await ctx.send("https://forum.gamer.com.tw/C.php?bsn=7650&snA=1021709&tnum=46")
        await ctx.send(file = self.send_picture("fp_archmage.png"))

    @commands.command()
    async def 惡復(self, ctx:commands.Context):
        await ctx.send(file = self.send_picture("devil_avg.png"))
    
    @commands.command()
    async def 練等(self, ctx:commands.Context):
        await ctx.send(file = self.send_picture("training.png"))

    @commands.command()
    async def 活動(self, ctx:commands.Context):
        ac_num = 4
        for i in range(1, ac_num + 1):
            pic_path = os.path.join("activity", f'ac_{i}.jpg')
            await ctx.send(file = self.send_picture(pic_path))

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))