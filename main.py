import discord
import os

client = discord.Client()

@client.event
# When the bot is ready
async def on_ready():
	print("Bot have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("$hello"):
		await message.channel.send("Hello!")

# client.run(os.environ('TOKEN'))

client.run(os.environ['TOKEN'])