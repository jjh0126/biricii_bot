import discord
import asyncio
import os
import discord
from discord.errors import ClientException
from discord.ext import commands
from discord import message  
bot = discord.Client()

@bot.event
async def on_message(message):
        if message.content == "!사용법":
                embed = discord.Embed(title="사용법은 아래를 보고 입력하면 된다 삐릭삐릭", description="!잘생긴사람   |   잘생긴 사람을 보여준다 삐릭 \n !너만든사람   |   날만든사람을 보여준다 삐릭\n !버전   |   나의 버전을 보여준다 삐릭\n !사용법   |   사용법을 보여준다 삐릭", color=0xF71317) 
                await message.channel.send(embed=embed)
        if message.content == "!잘생긴사람":
                embed = discord.Embed(title="잘생긴사람은...", description="김민찬이다 삐릭", color=0x62c1cc)
                await message.channel.send(embed=embed)
        if message.content == "!너만든사람":
                embed = discord.Embed(title="날만든사람은...", description="정준형이다 삐릭", color=0x49EDA0)
                await message.channel.send(embed=embed)
        if message.content == "!버전":
                embed= discord.Embed(title="나의버전은..", description="삐릭이_V2 1.0.0이다 삐릭", color=0xFCED20)
                await message.channel.send(embed=embed)



bot.run("ODcyMDUyMDM0MDQ2Njc2OTkz.YQkPvg.T9Y98LnzGkOlEVPqDbAA8cGcUWY")
