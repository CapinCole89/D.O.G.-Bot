import discord
import os
import random
from replit import db
from keep_alive import keep_alive
from message_handler import handle_response
import data_management as d_m


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
    handle_response(message)
    


keep_alive()
client.run(discord_token)
