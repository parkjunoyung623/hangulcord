import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == '안녕':
        await client.send_message(message.channel, '안녕!')
    if message.content.startswith('번역시작'):
        pass


client.run('NDM2MTU1MDA3OTE4ODAwOTA2.D282jQ.XbeJvtfHndSnZLHzrX4ZazDkUCY')