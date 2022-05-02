 # Description: Make the functionalities of the actual FerMIT bot

# Developers: Angel Magaña, Luis Inzunza

# State: Incompleted

# Previous bugs: none yet

import discord
from discord.ext import commands
import Info.info  

text = Info.info.Texts()

bot = commands.Bot( command_prefix = '!', 
description = "Hola, soy FerMIT, ¿En que puedo ayudarte?" )

@bot.command()
async def ayuda( ctx ):
    await ctx.send( text.help_message )

@bot.command()
async def comandos( ctx ):
    await ctx.send( text.comandos_message )

# Events
@bot.event
async def on_ready():
    print("My bot is ready")

bot.run('OTY4OTI5MTI5Njg2NzY5NzU0.Yml_kg.nhqz8msRsHxQh_SSZTEmkxOf148')

