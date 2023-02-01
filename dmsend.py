import discord
import asyncio
import datetime

client = discord.Client()

__TOKEN__ = 'MTA3MDIyNjQyMDc2NjM1MTM5MA.GkmGCJ.kf1Nzep5S7GOgbxDVqbm1uwmr04GEMai9GIbQk'
titlke = 'test bots'

@client.event
async def on_ready():
    print(client.user)
    #game = discord.Game('상태메시지')
    #await client.change_presence(status=discord.Status.online, activity=game)

#!디엠 {할말}
@client.event
async def on_message(message):
    if message.content.startswith('!디엠'):
        for i in message.guild.members:
            if i.bot:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(title=tile, description=msg, colour=discord.Colour.gold(), timestamp=message.created_at)
                        #embed.set_footer(text="맨 밑에 들어갈 내용")
                        await i.send(embed=embed)
                        print(f'{i} 전송')
                except:
                    pass


client.run(__TOKEN__)
