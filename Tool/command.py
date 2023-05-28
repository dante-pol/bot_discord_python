import discord
from discord.ext import commands
from system_data import command_prefix
import busingesslogic_data_base

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=command_prefix, intents=intents)

# information command -------------------------------------
@bot.command()
async def creater(ctx):# команда об информации о создателях
    await ctx.send(f"Данный бот был создан при поддержке компании ООО <<Школа программной инженерии>>\n"
                   f"программистами Зенин Василий и Евгений Невдах ")

@bot.command()
async def info(ctx):# информация о командах
    author = ctx.message.author
    await ctx.send(f'Привет, {author.mention}! У меня есть следующие команды :\n'
                   f'>att - вывод всех запланированных занятий\n'
                   f'>addtt (дд.мм.гггг час.минуты) - добавление нового занятия\n'
                   f'>ftt - предстоящее занятие\n'
                   f'>creater - информация о создателях')

# instrumental command -------------------------------------
@bot.command()
async def addtt(ctx, arg1, arg2):# команда добавления занятия
    author = ctx.message.author
    await ctx.send(busingesslogic_data_base.insert_date_lesson(arg1, arg2))

@bot.command()
async def att(ctx):# команда вывода всех занятий
    author = ctx.message.author
    await ctx.send(busingesslogic_data_base.insert_date_lesson())

@bot.command()
async def ftt(ctx): #  команда ближайщего занятия
    author = ctx.message.author
    await ctx.send(f"{author.mention}, ближайщее занятие запланировано на: ")