# Import Libraries for discord
import discord
import os # For token to work
from discord.ext import commands

# Import Libraries for console date/time messages
from datetime import datetime
from pytz import timezone 
import time

client = commands.Bot(command_prefix = "-") # Set the prefix for the bot
client.remove_command("help") # Remove default help command so custom can be used

# Gets current time for the console command log
def currentTimeEST():
	Eastern = timezone("US/Eastern")
	EST_Time = datetime.now(Eastern)

	return EST_Time.strftime("%H:%M:%S EST") # Formats the time correctly

# When bot starts
@client.event
async def on_ready():
	print("Bot is ready.")
	print(f"The current time is {currentTimeEST()}")
	print("Logged in as @{0.user}".format(client))
	print("----------\n")

# commands

@client.command()
async def ping(ctx): # Ping command
	print(f"Ping command was called at {currentTimeEST()} by {ctx.message.author}")
	await ctx.send(f"Pong! Latency of `{round(client.latency * 1000)}ms`.")	

@client.command()
async def help(ctx):
	print(f"Help command was called at {currentTimeEST()} by {ctx.message.author}")
	
	embed = discord.Embed(
		description = "*Please notethat this bot is currently under developement, so there may be bugs. If bugs happen, please let <@!624686837448835115> know.*",
		colour = 0xfce205
	)
	embed.add_field(name = "-help", value = "Displays this command.", inline = True)
	embed.add_field(name = "-ping", value = "Displays the latency of the bot.", inline = True)
	embed.add_field(name = "testing", value = "You have no value", inline = True)
	embed.add_field(name = "testing2", value = "You have no value", inline = True)

	await ctx.send(embed=embed)

@client.command()
async def clear(ctx, amount=5):
	print(f"Clear command was called at {currentTimeEST()} by {ctx.message.author}")
	time.sleep(1)
	await ctx.message.delete()
	await ctx.channel.purge(limit = amount)	
	
# Make bot run without rate limiting
try:
	client.run(os.environ['TOKEN'])
except:
  os.system("kill 1")