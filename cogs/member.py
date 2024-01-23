import discord
import os
import csv
import re

from datetime import datetime, timezone, timedelta
from discord.ext import commands


# load the picture from cogs/pic folder
def send_picture(pic_name):
    pic_path = os.path.join("cogs", "pic", pic_name)
    pic = discord.File(pic_path)
    return pic

# load the user's information from database.csv
def show_info(user_name):
    with open('cogs\database.csv', newline='', encoding='utf-8') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        list_data = list(rows)
    have_user = False
    for i in range(1, len(list_data)):
        if(list_data[i][0] == user_name):
            have_user = True
            user_info = list_data[i][1:]
            break
    return user_info if have_user else []

# attempt to update the information about the users. but updating the info by themselves. 
def update_info(user_name, attr, attr_info):
    if(attr == 'level'):
        if(check_level_format(attr_info)):
            return f'Your level format is wrong!!\n Correct format is **level_exp** (exp 到小數點後第三位).'
    elif(attr == 'hex_3'):
        if(check_hex_3_level(attr_info)):
            return f'Your hex_3 level format is wrong, please check **num1-num2-num3-num4**.'
    info = [attr, attr_info]
    r = csv.reader(open('cogs\database.csv', encoding='utf-8'))
    lines = list(r)
    field = lines[0]
    if info[0] not in field:
        return f'Error...Have not {info[0]} attribute.'
    for line in lines:
        if(line[0] == user_name):
            line[field.index(info[0])] = info[1]
    with open('cogs\database.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)
    return f'Updated {user_name}\'s {info[0]} done.'

# level's format: level_exp, level can't empty, and then exp is round up to the third decimal (ex. 265_28.733).
def check_level_format(level_str: str):
    if('_' not in level_str):
        return True
    tmp = level_str.split('_')
    if(len(tmp[1]) != 6 or len(tmp[0]) == 0):
        return True
    
    return False

def check_hex_3_level(level_str: str):
    if(level_str.count('-') != 3):
        return True
    return False

# compute the corresponding elda pieces to the hexa skill level.
def compute_elda(hex_1_level: int , hex_2_level: int, hex_3_level: list):
    hex_1 = [0, 30, 35, 40, 45, 50, 55, 60, 65, 200, 80, 90, 100, 110, 120, 130, 140, 150, 160, 350, 170, 180, 190, 200, 210, 220, 230, 240, 250, 500]
    hex_2 = [50, 15, 18, 20, 23, 25, 28, 30, 33, 100, 40, 45, 50, 55, 60, 65, 70, 75, 80, 175, 85, 90, 95, 100, 105, 110, 115, 120, 125, 250]
    hex_3 = [75, 23, 27, 30, 34, 38, 42, 45, 49, 150, 60, 68, 75, 83, 90, 98, 105, 113, 120, 263, 128, 135, 143, 150, 158, 165, 173, 180, 188, 375]
    hex_3_level = [int(num) for num in hex_3_level]
    hex_3_sum = 0
    for level in hex_3_level:
        hex_3_sum += sum(hex_3[:level])
    return sum(hex_1[:hex_1_level]) + sum(hex_2[:hex_2_level]) + hex_3_sum

# 定義名為 Info 的 Cog
class Member(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    # 前綴指令
    @commands.command(brief = "- He just like a monkey...")
    async def 莊明輯(self, ctx:commands.Context):
        await ctx.send(file = send_picture("monkey.jpg"))
        await ctx.send(file = send_picture("monkey_mouse.gif"))
    
    @commands.command(brief="- Show your own information about MS.", description="$show [user_id]\n If no user id, show your own information.")
    async def show(self, ctx:commands.Context, user_name = None):
        name_str = ctx.author.name if user_name is None else user_name
        user_info = show_info(name_str)
        if(len(user_info)):
            embed=discord.Embed(title="TMS information", url="https://youtu.be/OIBODIPC_8Y?si=zHqG8qvIYJGutWQc", description="About TMS", 
                                color=0x60e176, timestamp=datetime.now())
            embed.set_author(name=ctx.author.global_name, url="https://maplestory.beanfun.com/main")
            pic_path = os.path.join("cogs", "pic", user_info[4])
            pic_file = discord.File(pic_path)
            embed.set_thumbnail(url=f"attachment://{user_info[4]}")
            embed.add_field(name="遊戲名稱", value=user_info[0], inline=False)
            embed.add_field(name="伺服器", value=user_info[1], inline=False)
            embed.add_field(name="職業", value=user_info[2], inline=True)
            level_exp = user_info[3].split('_') 
            embed.add_field(name="等級", value=f'{level_exp[0]} ({level_exp[1]}%)', inline=True)
            embed.add_field(name="聯盟戰地", value=user_info[5], inline=True)
            hex_list = user_info[6].split('-')
            embed.add_field(name=hex_list[0], value=user_info[7], inline=True)
            embed.add_field(name=hex_list[1], value=user_info[8], inline=True)
            hex_3_level = user_info[9].split('-')
            j = 0
            for i in range(2, 6):
                embed.add_field(name=hex_list[i], value=hex_3_level[j], inline=True)
                j += 1
            total = compute_elda(int(user_info[7]), int(user_info[8]), hex_3_level)
            embed.add_field(name="技能已使用愛爾達碎片(總進度)", value=f'**{total}** ({round((total/20183)*100, 2)}%)', inline=False)
            embed.set_footer(text="Have fun.")
            await ctx.send(file=pic_file, embed=embed)
        else:
            await ctx.send(f"這位玩家沒有玩楓之谷啦...")
    
    @commands.command(brief = "- Update your own information about MS.", description = "$update [attribution] [attribition_info]\n attributtion list: game_name/server/job/level/gruop(聯盟戰地)/hex_1(起源技能)/hex_2(精通技能)/hex_3(五轉四技)(ex 10-6-2-7)\n")
    async def update(self, ctx:commands.Context, attr, attr_info):
        name_str = ctx.author.name
        updated_status = update_info(name_str, attr, attr_info)
        await ctx.send(updated_status)

    @commands.command(brief = "- Record training status.", description = "$record_level [training space] [spend_time] [elda piece] [current level and exp] [money] [item_drop] [money_drop]")
    async def record_level(self, ctx:commands.Context, space: str, time, piece: int, cur: str, money: str, item_drop, money_drop):
        if(check_level_format(cur)):
            await ctx.send(f'Your level format is wrong!!\n Correct format is **level_exp** (exp 到小數點後第三位).')
            return
        
        name_str = ctx.author.name
        # Record time
        str_datetime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

        # Read level and exp in the past.
        r = csv.reader(open('cogs\database.csv', encoding='utf-8'))
        lines = list(r)
        for line in lines:
            if(line[0] == name_str):
                before = line[4]
                game_name = line[1]
                before_piece = int(line[11])

        before_level_exp = before.split('_')
        before_level, before_exp = before_level_exp[0], before_level_exp[1]

        # Construct level and exp currently.
        cur_level_exp = cur.split('_')
        cur_level, cur_exp = cur_level_exp[0], cur_level_exp[1]
        if(cur_level < before_level):
            await ctx.send('Your level input is wrong!! Your level is back to lower.')
            return
        # level up!! congrates!
        if(cur_level > before_level):
            update_exp = f"{before_level}: {round(100.000-float(before_exp), 3)}%, {cur_level}: {round(float(cur_exp), 3)}%"
            await ctx.send('**Congrates! Level up!! CCCCCCC...**') 
        else:
            update_exp = f"{cur_level}: {round(float(cur_exp) - float(before_exp), 3)}%"

        update_piece = piece - before_piece
        # Write the data into the record csv.
        record_data = [name_str, str_datetime, space, time, update_piece, update_exp, money, item_drop, money_drop]
        record_level_file = os.path.join('cogs', 'record.csv')
        with open(record_level_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(record_data)

        show_text = f'{game_name} {str_datetime}\n- 地圖: {space}\n- 練等時間: {time} HR\n- 愛爾達碎片獲取量: {update_piece}\n- 經驗提升量: {update_exp}\n- 獲取金錢數: {money}\n- 道具掉落率: {item_drop} %\n- 楓幣掉落率: {money_drop} %.'
        await ctx.send(show_text)

        # Final, update the level information in database.csv
        updated_status = update_info(name_str, 'level', cur)
        updated_status = update_info(name_str, 'piece', update_piece)
        await ctx.send(f'Record of training status is done! Thank you~ :D')


# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Member(bot))