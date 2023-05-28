import discord
import system_data
import businesslogic
from businesslogic import DefaultCommand
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)



@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def att(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'руддщ')


@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def info(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Привет, {author.mention}! У меня есть следующие команды :\n'
                   f'$att - вывод всех запланированных занятий\n'
                   f'$addtt (дд.мм.гггг час.минуты) - добавление нового занятия\n'
                   f'$ftt - предстоящее занятие')

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def addtt(ctx, arg1, arg2): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'{arg1} {arg2}')

# token = input("input token :")
# bot.run(token)
