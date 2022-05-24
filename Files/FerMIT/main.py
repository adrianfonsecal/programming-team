# Description: Make the functionalities of the actual FerMIT bot
# Developers: Angel Magaña, Luis Inzunza, David Perez, Luis Medina
# Bugs: 1
# State: In progress

import os
from discord.ext import commands
import src.Info.Files.info
from Fermit.BotRunner.webserver import keep_alive
text = src.Info.info.Texts()

# Secret Token
TOKEN = os.environ.get("FerMIT_Secret")

# Bot commands
bot = commands.Bot( command_prefix = '!', 
description = "Hola, soy FerMIT, ¿En que puedo ayudarte?" )

bot.remove_command( 'help' )

# Requerimientos Funcionales Main

@bot.command()
async def help( ctx ):
  await ctx.send(embed=text.hola_message )
  #Terminado

@bot.command()
async def ayuda( ctx ):
  await ctx.send(embed=text.hola_message )
  #Terminado

@bot.command()
async def comandos( ctx ):
  await ctx.send(embed=text.comandos_message )
  #terminado
  
@bot.command()
async def tramites( ctx ):
  await ctx.send(embed=text.tramites_message )
  #En proceso

@bot.command()
async def mapa( ctx ):
  await ctx.send(embed=text.mapa_message )
  #Falta el croquis

@bot.command()
async def informacion( ctx ):
  await ctx.send(embed=text.informacion_message )
  #Terminado

@bot.command()
async def relevante( ctx ):
  await ctx.send(embed=text.relevante_message )
  #Terminado, debe ser actualizado con frecuencia

# Requerimientos Tramites

@bot.command()
async def revalidacion( ctx ):
  await ctx.send(embed=text.revalidacion_message )
  await ctx.send(embed=text.revalidacion_message_2 )
  #Por revisar y enlistado

@bot.command()
async def revalidacionCIL( ctx ):
  await ctx.send(embed=text.revalidacionCIL_message )
  #Terminado y enlistado

@bot.command()
async def inscripcion( ctx ):
  await ctx.send(embed=text.inscripcion_message)
  #Terminado y enlistado

@bot.command()
async def reinscripcion( ctx ):
  await ctx.send(embed=text.reinscripcion_message)
  #Terminado y enlistado

@bot.command()
async def descargaMaterias( ctx ):
  await ctx.send(embed=text.descargaLibres_message )
  await ctx.send(embed=text.descargaOptativas_message )
  #Falta investigar y enlistado

@bot.command()
async def constancia( ctx ):
  await ctx.send(embed=text.constancia_message )
  #Terminado y enlistado

@bot.command()
async def certificado( ctx ):
  await ctx.send(embed=text.certificado_message )
  #Terminado y enlistado

@bot.command()
async def adeudoConta( ctx ):
  await ctx.send(embed=text.adeudoConta_message )
  
@bot.command()
async def adeudoBiblio( ctx ):
  await ctx.send(embed=text.adeudoBiblio_message )

@bot.command()
async def titulacion( ctx ):
  await ctx.send(embed=text.titulacionMEFI_message )
  #Terminado y enlistado

@bot.command()
async def tituEGEL( ctx ):
  await ctx.send(embed=text.tituEGEL_message )
  #Terminado

@bot.command()
async def tituTesis( ctx ):
  await ctx.send(embed=text.tituTesis_message )
  #Terminado

@bot.command()
async def tituDirecta( ctx ):
  await ctx.send(embed=text.tituDirecta_message )
  #Terminado y enlistado

# Requerimientos de informacion de importancia

@bot.command()
async def calendario( ctx ):
  await ctx.send(embed=text.calendario_message )
  #Terminado, Enero-Mayo
  
@bot.command()
async def ciscoAcademy( ctx ):
  await ctx.send(embed=text.ciscoAcademy_message )

@bot.command()
async def bajasAcademicas( ctx ):
  await ctx.send(embed=text.bajasAcademicas_message )

@bot.command()
async def bloquesCarga( ctx ):
  await ctx.send(embed=text.bloquesCarga_message )  
  
# Events
@bot.event
async def on_ready():
  print("FerMIT is ready")

# Bot runner
keep_alive()
bot.run(TOKEN)