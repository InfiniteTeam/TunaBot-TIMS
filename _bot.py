import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('InfinieTEAM'))
    
@client.event
async def on_message(message):
    if message.content.startswith('hu'):
        await message.channel.send('dwdw')
    
client.run('NTE2MTY3NDY4NjEyNDUyMzc5.Xj-KwQ.uY8vGD5C3QkaA_qT2xoVZNW-8BU')