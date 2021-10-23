import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

hi = ["hi","Hi","hoi","Hoi","hello","Hello"]

call_words = ["manda","Manda","Mandan","mandan","mandaa","Mandaa"]

hi_replies = ["Hi mona","Hi gooys sugalle","Hoi"]

reply= ["Entha mona","Yesh","sorry mona","Enthada","Aahda","Aah mona"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if any(word in msg for word in hi):
    await message.channel.send(random.choice(hi_replies))

  if any(word in msg for word in call_words):
    await message.channel.send(random.choice(reply)) 

keep_alive()
client.run(os.getenv('TOKEN'))