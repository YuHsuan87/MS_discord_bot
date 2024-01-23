# MS_discord_bot
The discord bot about maplestory.

## Enviroment
- Python version: 3.10.0
- discord.py 2.3.2

## 練等紀錄懶人包
讓我的資料庫蒐集一下...🙏
- 先去:
```
$update level [等級_當前趴數(小數點後三位)]
```
- 查看當前愛爾達碎片量，並在過程中不要使用，如需使用至少幫我記得用多少。
- 將錢投入倉庫內，最後在記錄錢的部分會比較好算~
- 練等結束後，依序輸入:
```
$record_level [地點] [練等時間] [碎片掉落] [當前等級與趴數] [金幣獲得量] [道具掉落率] [楓幣掉落率]
```
如果顯示:
![image](https://github.com/YuHsuan87/MS_discord_bot/blob/main/readmd_pic/readmd_1.png)

即代表完成，未顯示代表輸入有誤 (不知道錯在哪可以直接問我)。

## How to use in detail (不定期更新)
### Check the commands and its information.
```
$help
```
If you want to check **``update''** command.
```
$help update
```
It can see the description and its args need to input.

**If any argument forget to input, this command will not implement!!**

### Show the user's information in database.
```
$show [user_id in the server]
```
if you are not input the **user_id** (not user_name), then will show your own information about your character.
We display character information through **discord embeded**.
like the example below:
![image](https://github.com/YuHsuan87/MS_discord_bot/blob/main/readmd_pic/readmd_2.jpg)

### Update your own character's information
```
$update [attribute] [attribute_information]
```
Ex.
```
$update level 280_73.885
```
#### Attributes info
|     Attribute      |                   notice                   |
|:------------------:|:------------------------------------------:|
|     game_name      |                                            |
|       server(伺服器)       |                                            |
|     job (職業)     |                                            |
|       level        | 等級_當前趴數: 280_15.998 (小數點後第三位) |
|  group (聯盟戰地)  |                                            |
| hex_1  (起源技能)  |                                            |
| hex_2  (精通技能)  |                                            |
| hex_3   (五轉四技) |    五轉一技-五轉二技...(共四個數字)                                        |

### Record training status.
Try to record training and other situations, commonly known as **"坐牢紀錄器"**
```
$record_level [地點] [練等時間] [碎片掉落] [當前等級與趴數] [金幣獲得量] [道具掉落率] [楓幣掉落率]
```
**Notice: 當前等級與趴數輸入要求與上面 update format 相同。**

### Others info
```
$[info]
```
Ex.
```
$破風
```


