import discord
from discord.ext import commands
import random
import math
import os

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot("%", case_insensitive = True)

client.remove_command('help')


@client.event
async def on_ready():
  print ("to on")

@client.command(name="d4")
async def roll_d4(ctx, quant):
  randomlist = []
  for i in range (0,int(quant)):
        n = random.randint(1,4)
        randomlist.append(n)
  await ctx.send(f"{randomlist}")

@client.command(name="d6")
async def roll_d6(ctx, quant):
  randomlist = []
  for i in range (0,int(quant)):
        n = random.randint(1,6)
        randomlist.append(n)
  await ctx.send(f"{randomlist}")

@client.command(name="d8")
async def roll_d8(ctx, quant):
  randomlist = []
  for i in range (0,int(quant)):
        n = random.randint(1,8)
        randomlist.append(n)
  await ctx.send(f"{randomlist}")

@client.command(name="d10")
async def roll_d10(ctx, quant):
  randomlist = []
  for i in range (0,int(quant)):
        n = random.randint(1,10)
        randomlist.append(n)
  await ctx.send(f"{randomlist}")

@client.command(name="d12")
async def roll_d12(ctx, quant):
  randomlist = []
  for i in range (0,int(quant)):
        n = random.randint(1,12)
        randomlist.append(n)
  await ctx.send(f"{randomlist}")

@client.command(name="d20")
async def roll_d20(ctx, quant):
  randomlist = []
  for i in range (0,int(quant)):
        n = random.randint(1,20)
        randomlist.append(n)
  await ctx.send(f"{randomlist}")

@client.command(name="d100")
async def roll_d100(ctx, quant):
  randomlist = []
  for i in range (0,int(quant)):
        n = random.randint(1,100)
        randomlist.append(n)
  await ctx.send(f"{randomlist}")

@client.command(name="mpf")
async def metrospf (ctx, quant):
  res = int(quant) / 1.5
  resultado = int(res) * 5
  await ctx.send(f"{resultado}")

@client.command(name="fpm")
async def feetspm (ctx, quant):
  res = int(quant) / 5
  resultado = int(res) * 1.5
  await ctx.send(f"{resultado}")

@client.command(name="mpq")
async def metrospq (ctx, quant):
  resultado = int(quant) / 1.5
  await ctx.send(f"{resultado}")

@client.command(name="qpf")
async def quadradopf (ctx, quant):
  resultado = int(quant) * 5
  await ctx.send(f"{resultado}")

@client.command(name="qpm")
async def quadradopm (ctx, quant):
  resultado = int(quant) *1.5
  await ctx.send(f"{resultado}")

@client.command(name="fpq")
async def feetspq (ctx, quant):
  resultado = int(quant) / 5
  await ctx.send (f"{resultado}")

@client.command(name="h")
async def hipote (ctx, caad, caop):
  adjacente = int(caad) * int(caad)
  oposto = int(caop) * int(caop)
  semi = oposto + adjacente
  hipo = math.sqrt(semi)
  await ctx.send (f"{hipo}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("OTAyMTk0NTYzNDU4OTQ5MTMx.YXa4KQ.pP9klgpQ4hqQwVzeChsz0fFRlqc")