# Import Libraries for discord
import discord
import os # For token to work
from discord.ext import commands

# Import Libraries for console date/time messages
from datetime import datetime
from pytz import timezone 

client = commands.Bot(command_prefix = "-") # Set the prefix for the bot
client.remove_command("help") # Remove default help command so custom can be used

# Gets current time for the console command log
def currentTime():
	Eastern = timezone("US/Eastern")
	EST_Time = datetime.now(Eastern)

	return EST_Time.strftime("%H:%M:%S EST")

	
# When bot starts
@client.event
async def on_ready():
	print("Bot is ready.")
	print("Logged in as @{0.user}".format(client))
	print("----------\n")
	
# Atominous bot things
@client.event
async def on_member_join(member):
	print(f"{member} has joined the server! Say hello!")
@client.event
async def on_member_remove(member):
	print(f"{member} doesn't want to stay on the server! Say goodbye!")
	

# commands
@client.command()
async def ping(ctx):
	print(f"Ping command was called at {currentTime()}")
	await ctx.send(f"Pong! Latency of `{round(client.latency * 1000)}ms`.")	

@client.command()
async def help(ctx):
	print(f"Help command was called at {currentTime()}")
	
	embed = discord.Embed(
		description = "*Please notethat this bot is currently under developement, so there may be bugs. If bugs happen, please let <@!624686837448835115> know.*",
		colour = 0xfce205
	)
	embed.add_field(name = "-help", value = "Displays this command.", inline = True)
	embed.add_field(name = "-ping", value = "Displays the latency of the bot.", inline = True)
	embed.add_field(name = "testing", value = "You have no value", inline = True)
	embed.add_field(name = "testing2", value = "You have no value", inline = True)

	await ctx.send(embed=embed)

	
# Make bot run without rate limiting
try:
	client.run(os.environ['TOKEN'])
except:
    os.system("kill 1")