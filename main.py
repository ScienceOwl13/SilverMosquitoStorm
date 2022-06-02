import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "-")
client.remove_command("help")

# Random Variables
rickRollURL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

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
	print("Ping command was called")
	await ctx.send(f"Pong! Latency of `{round(client.latency * 1000)}ms`.")	

@client.command()
async def help(ctx):
	print("Help command was called")

	embed = discord.Embed(
		description="""
		*This bot is currently under developement, so the commands are limited*
		\n
		**Current Commands:**
		- Help
		  - Displays this pannel
		- Ping
		  - Displays bot latency.
		"""
	)
	await ctx.send(embed=embed)

@client.command()
async def embed(ctx):
	embed = discord.Embed(
		description = "*Please notethat this bot is currently under developement, so there may be bugs and fun stuff*",
		colour = discord.Colour.blue()
	)
	embed.add_field(name = "two", value = "Displays this command.", inline = True)

	await ctx.send(embed=embed)

	
# Make bot run without rate limiting
try:
	client.run(os.environ['TOKEN'])
except:
    os.system("kill 1")