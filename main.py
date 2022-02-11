import discord
import os
from replit import db
from keep_alive import keep_alive
from message_handler import handle_response


discord_token = os.environ['Token']
client = discord.Client()


if "responding" not in db.keys():
    db["responding"] = True


# This initialises the bot and returns a confirmation in the terminal
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# This initialises when a message comes into the server
@client.event
async def on_message(message):
    bot_response = handle_response(message)

    if bot_response:
      await message.channel.send(bot_response)


keep_alive()
client.run(discord_token)
