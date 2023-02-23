

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# For bot to work it has to print 'Bot has started'
@client.event
async def on_ready():
    print('Bot has started')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('YOUR TOKEN HERE')
