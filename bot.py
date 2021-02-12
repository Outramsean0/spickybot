import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('admin$stop'):
        await client.logout()
#hello command
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('Hello!'):
        await message.channel.send('Hello!')
    if message.content.startswith('hello!'):
        await message.channel.send('Hello!')
    if message.content.startswith('!buy!'):
        await message.channel.send('open a tyciket in the ticket channel')
client.run('ODAzMTc4OTc3OTEyMjkxMzU4.YA6Atg.CsT-mGZLU1Ocs6aUAhb5Ey2I6fE')
