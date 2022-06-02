import discord
import os

client = discord.Client()

@client.event

# When the bot is ready
async def on_ready():
	print("The bot has succesfully logged in as @{0.user}".format(client))

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