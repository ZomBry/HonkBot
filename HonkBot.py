import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime

bot = commands.Bot(command_prefix='!', case_insensitive=True)

def TimeStamp(nameOfMsg):
    print(nameOfMsg + " Message Sent at ", end="")
    print(datetime.now().time())

@bot.event
async def on_ready():
    print("Ready to go!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

@bot.command(pass_context=True)
async def honk(ctx, *, msg: str):
    emoji = '<:honk:632089129735290900>'
    embed = discord.Embed()
    embed.set_image(url="https://cdn.discordapp.com/attachments/566888125356572673/654746537833791519/big_honk.jpg")
    await ctx.send(embed=embed)
    await ctx.send(emoji + " " +  msg + " " + emoji)
    TimeStamp("Command_Honk")

@bot.event
async def on_message(message):    
    noSpaceMessage = str(message.content.replace(" ","").lower())
    if message.author == bot.user:
          return
    
    if "honk" in noSpaceMessage and not "thonk" in noSpaceMessage and not "!honk" in noSpaceMessage:
        emoji = '<:honk:632089129735290900>'
        await message.add_reaction(emoji)
        TimeStamp("Honk")
        
    await bot.process_commands(message)
    
from key import bot_token
bot.run(bot_token)


