import discord
import os
bot = discord.Client()
johnjal = os.environ['Johnjal']
maker = os.environ['Maker']

@bot.event
async def on_message(message):
        ch = bot.get_channel(872314637071310848)
        if message.content == "!사용법":
                embed = discord.Embed(title="사용법은 아래를 보고 입력하면 된다 삐릭삐릭", description="!잘생긴사람   |   잘생긴 사람을 보여준다 삐릭 \n !너만든사람   |   날만든사람을 보여준다 삐릭\n !버전   |   나의 버전을 보여준다 삐릭\n !사용법   |   사용법을 보여준다 삐릭\n!사용법2   |   사용법2를 보여준다삐릭", color=0xF71317) 
                await message.channel.send(embed=embed)
        if message.content == "!잘생긴사람":
                embed = discord.Embed(title="잘생긴사람은...", description= johnjal, color=0x62c1cc)
                await message.channel.send(embed=embed)
        if message.content == "!너만든사람":
                embed = discord.Embed(title="날만든사람은...", description= maker, color=0x49EDA0)
                await message.channel.send(embed=embed)
        if message.content == "!버전":
                embed= discord.Embed(title="나의버전은..", description="삐릭이_V2 1.0.0이다 삐릭", color=0xFCED20)
                await message.channel.send(embed=embed)
        if message.content == "!사용법문의":
                embed= discord.Embed(title="문의사용법은..", description="1. 문의할때 띄어쓰기는 __로 해야한다\n2. 사용예시: !문의 문의예시다삐릭 \n3. 봇에 대한 문의를 사용하는것이다 삐릭", color=0xEEE15B)
                await message.channel.send(embed=embed)
        if message.content == "!사용법2":
                embed= discord.Embed(title="사용법2다 삐릭", description="!사용법문의   |   문의사용법을 보여준다 삐릭 문의할때는 무조건 보고하여라 삐릭\n", color=0xAC3AD5)
                await message.channel.send(embed=embed)

        if message.content.startswith("!문의"):
              msg_l = message.content.split()
              try:
                  data = msg_l[1]
              except:
                  await message.channel.send("내용을 입력해주세요!")
                  return
              ch = bot.get_channel(876290839133949992)
              await ch.send (data.format(message.author, message.author.mention))


acces_token = os.environ['BOT_TOKEN']
bot.run(acces_token)
