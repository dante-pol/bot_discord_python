from info_command import bot


@bot.command()
async def addtt(ctx, arg1, arg2): # функция добавления учебного занятия
    author = ctx.message.author
    await ctx.send(f'{arg1} {arg2}')

@bot.command()
async def att(ctx): # функция вывода всех команд
    author = ctx.message.author
    await ctx.send(f'руддщ')