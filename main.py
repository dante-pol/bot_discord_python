import discord
import bot_data
import businesslogic
from businesslogic import DefaultCommand

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

    if businesslogic.check_command_prefix(message.content):
        await message.channel.send(businesslogic.DefaultCommand.start_pars_to_message(message.content))
    else:
        text = DefaultCommand.start_pars_to_message(message.content)
        await message.channel.send(text)



client.run(bot_data.token)
