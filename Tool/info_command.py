import discord
from discord.ext import commands
from system_data import command_prefix

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=command_prefix, intents=intents)

@bot.command()
async def creater(ctx): # информация о создателях
    await ctx.send(f"Данный бот был создан благодаря поддержке компании ООО <<Школа программной инженерии>>\n"
                   f"программистами Зенин Василий и Евгений Невдах ")

@bot.command()
async def info(ctx): # информация о командах
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Привет, {author.mention}! У меня есть следующие команды :\n'
                   f'$att - вывод всех запланированных занятий\n'
                   f'$addtt (дд.мм.гггг час.минуты) - добавление нового занятия\n'
                   f'$ftt - предстоящее занятие')