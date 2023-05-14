import discord
import bot_data
import businesslogic
from businesslogic import DefaultCommand
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = bot_data.command_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if businesslogic.check_command_prefix(message.content):
        await message.channel.send(businesslogic.DefaultCommand.start_pars_to_message(message.content))
    else:
        text = DefaultCommand.start_pars_to_message(message.content)
        await message.channel.send(text)


@bot.command()
async def timetable(ctx, key):
    await ctx.send(key)

bot.run(bot_data.token)
