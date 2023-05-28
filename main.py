import discord
import system_data
import businesslogic
from businesslogic import DefaultCommand
from discord.ext import commands


@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def att(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'руддщ')



@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def addtt(ctx, arg1, arg2): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'{arg1} {arg2}')


# token = input("input token :")
# bot.run(token)
