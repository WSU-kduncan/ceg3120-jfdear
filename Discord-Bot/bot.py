import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    deathnote_quotes = [
        'L, did you know? Gods of death love apples' ,
        'The human world is a boring place with boring people doing boring things.' ,
        'Laws aren’t perfect, because humans who created laws aren’t perfect. It’s impossible to be perfect. However, the laws are evidence of the human’s struggle to be righteous.' ,
        'Learn to treasure your life because unfortunately, it can be taken away from you anytime.' ,
        'You can’t ever win if you’re always on the defensive. To win, you have to attack!' ,
        'In This World, There Are Very Few People Who Actually Trust Each Other.' ,
        'An Eye For An Eye, My Friend.' ,
        'In The End, There Is No Greater Motivation Than Revenge.' ,

    ]

    if message.content == '!dnote':
        response = random.choice(deathnote_quotes)
        await message.channel.send(response)

client.run(TOKEN)
