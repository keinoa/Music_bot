import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event

#async為協成函式,重新定義功能時使用
async def on_ready():
    print(">> Bot is online <<")

#token可能會報錯
bot.run('NDU5Njc5NjI3Njk5NDIxMTg0.WyzcAw.TTGNWK8qtQ23bVYu10kS37WO9B8')
