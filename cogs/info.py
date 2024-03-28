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
        path = os.path.join("hex_point", "wind_archer.png")
        await ctx.send(file = self.send_picture(path))

    @commands.command()
    async def 開拓(self, ctx:commands.Context):
        await ctx.send("https://forum.gamer.com.tw/C.php?bsn=7650&snA=1012750")
        path = os.path.join("hex_point", "pathfinder.jpg")
        await ctx.send(file = self.send_picture(path))

    @commands.command()
    async def 阿戴爾(self, ctx:commands.Context):
        path = os.path.join("hex_point", "adale.png")
        await ctx.send(file = self.send_picture(path))

    @commands.command()
    async def 主教(self, ctx:commands.Context):
        await ctx.send("https://forum.gamer.com.tw/C.php?bsn=7650&snA=1021664")
        path = os.path.join("hex_point", "bishop.png")
        await ctx.send(file = self.send_picture(path))

    @commands.command()
    async def 火毒(self, ctx:commands.Context):
        await ctx.send("https://forum.gamer.com.tw/C.php?bsn=7650&snA=1021709&tnum=46")
        path = os.path.join("hex_point", "fp_archmage.png")
        await ctx.send(file = self.send_picture(path))

    @commands.command()
    async def 惡復(self, ctx:commands.Context):
        path = os.path.join("hex_point", "devil_avg.png")
        await ctx.send(file = self.send_picture(path))
    
    @commands.command()
    async def 練等(self, ctx:commands.Context):
        await ctx.send(file = self.send_picture("training.png"))
    
    @commands.command()
    async def 里程碑(self, ctx:commands.Context):
        text = "```普通 - 賽蓮: 2024/01/27\n成員: 蔡倫reason、跟隨風的使者```"
        await ctx.send(text)
        path_1 = os.path.join("boss", "normal_seren_1.jpg")
        path_2 = os.path.join("boss", "normal_seren_2.jpg")
        await ctx.send(files = [self.send_picture(path_1), self.send_picture(path_2)])
        text = "```困難 - 賽蓮: 2024/03/03\n成員: 蔡倫reason、跟隨風的使者、一修逆鴨肉```"
        await ctx.send(text)
        path_1 = os.path.join("boss", "hard_seren_1.jpg")
        path_2 = os.path.join("boss", "hard_seren_2.jpg")
        await ctx.send(files = [self.send_picture(path_1), self.send_picture(path_2)])
        text = "```困難 - 黑魔法師: 2024/02/26\n成員: 蔡倫reason、跟隨風的使者、一修逆鴨肉```"
        await ctx.send(text)
        path_1 = os.path.join("boss", "black_magician_1.png")
        path_2 = os.path.join("boss", "black_magician_2.png")
        await ctx.send(files = [self.send_picture(path_1), self.send_picture(path_2)])
        text = "```簡單 - 卡洛斯: 2024/03/03\n成員: 蔡倫reason、跟隨風的使者、一修逆鴨肉、SnowScript戴```"
        await ctx.send(text)
        path_1 = os.path.join("boss", "easy_dog_1.jpg")
        path_2 = os.path.join("boss", "easy_dog_2.jpg")
        await ctx.send(files = [self.send_picture(path_1), self.send_picture(path_2)])

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))