import discord
from discord.utils import get
import random
import asyncio
from discord.ext import commands
import gsheets_connection


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot('!', intents=intents)

gsheets = gsheets_connection

#Print Bot name and id
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    

#Function to return a list with playes with that specific Role
@bot.command()
async def x5lol(ctx):    
    """Teste"""
    #Shortcut to Author of the Message
    atr = ctx.author
    #Shortcut to Author Current Voice Channel
    currentvc = atr.voice.channel.name
    #Shortcut to Voice Channel Members list
    usrs = atr.voice.channel.members
    #Specify what role will use 
    role = ctx.guild.get_role("""Insert role id""")
    
    pot = []
    #await ctx.send(atr.name +'   '+currentvc)
    for i in usrs:
        if role in i.roles:
            #await ctx.send('O  ' + str(i) + '  É  ' + str(role))
            nick = (str(i.nick))
            if nick != 'None':
                 pot.append(str(i.nick))
            else:
                pot.append(str(i))
    
              
    #NOTE:The math part of team ballance isn't done yet
    # For now, Bot shuffle the names, then send to Text Channel on Discord         
    random.shuffle(pot)
    await ctx.send(pot)


@bot.command()
async def x5cs(ctx):    
    """Teste"""
    atr = ctx.author
    currentvc = atr.voice.channel.name
    usrs = atr.voice.channel.members
    role = ctx.guild.get_role("""Insert role id""")
    pot = []
    
    #await ctx.send(atr.name +'   '+currentvc)
    for i in usrs:
        if role in i.roles:
            #await ctx.send('O  ' + str(i) + '  É  ' + str(role))
            nick = (str(i.nick))
            if nick != 'None':
                 pot.append(str(i.nick))
            else:
                pot.append(str(i))

              
    #print(pot)            
    random.shuffle(pot)
    await ctx.send(pot)    



@bot.command()
async def diaschurras(ctx):
    days = gsheets.main('days')
    data = gsheets.main('data')
    await ctx.send(f'A data mínima do churras é {data} e faltam {days} dias!')

@bot.command()
async def segundadose(ctx, message):
    data = gsheets.dataframe('2dose', message)
    days = gsheets.dataframe('days_to', message)
    await ctx.send(f'A data da segunda dose do **{message}** é **{data}** e faltam {days} dias para imunização total.')

@bot.command()
async def tabelavacina(ctx):
    await ctx.send("""Link to gsheets""")

@bot.command()
async def comandos(ctx):
    await ctx.send('Os comandos atuais do **Guardiola** são: \n **!x5lol** : Seleciona membros com cargo de LoL e separa **aleatoriamente** em 2 times \n'
    + '**!x5cs** : Seleciona membros com cargo de CS e separa **aleatoriamente** em 2 times \n'
    + '**!diaschurras** : Retorna possível data mínima de imunizaçao total do grupo e quantos dias faltam \n'
    + '**!segundadose** (incluir nome do membro) : Retorna data mínima da segunda dose e dias para imunizaçao \n'
    + '**!tabelavacina** : Retorna link da tabea de vacinação (também está fixada no discord)')


#Connect bot to discord
try:
    bot.run("""bot-token""")
except Exception as e:
    raise e