import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('Hi'):
    await message.channel.send('Hi')
    await message.channel.send('Hi')
    await message.channel.send('Hi gooys sugalle')
    

client.run(os.getenv('TOKEN'))