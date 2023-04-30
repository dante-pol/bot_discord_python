import discord
import bot_data

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(command_prefix = bot_data.command_prefix, intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if bot_request_hello(message.content):
        await message.channel.send('Hello! I am Alex!')


def bot_request_hello(txt: str):
    lst = ["hi", "hello", "good", "hey"]
    if txt.startswith('$'):
        for i in lst:
            if i in txt:
                return True
    return False


client.run(bot_data.token)
