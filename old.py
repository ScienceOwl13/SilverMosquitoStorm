import discord
from discord.ext import commands
import os

client = discord.Client()

@client.event

# When the bot is ready
async def on_ready():
	print("The bot has succesfully logged in as @{0.user}".format(client))

bot = commands.Bot(command_prefix='!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command(name='info')
async def helpCommand(message):
	await message.channel.send("Hello World")
	
#Say hello when '$hello' is sent
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("$hello"):
		await message.channel.send("Hello!")

# Prevents rate limiting
try:
	client.run(os.environ['TOKEN'])
except:
    os.system("kill 1")