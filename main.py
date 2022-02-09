import discord
import os
import random
from replit import db
from keep_alive import keep_alive
import reply
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
  # This ignores messages from the bot
  if message.author == client.user:
    return

  msg = message.content.lower()
  author = str(message.author)
  friend = author[0: -5]


  #This sends a quote from above when asked to inspire
  if msg.startswith('$inspire'):
    quote = reply.get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    encouragements = []
    poems = []

    # This sets the list of encouragements
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]

    # This sets the list of poems
    if "haikus" in db.keys():
      poems = db["haikus"]

    # This will see is a message contains a sad word, then responds
    if any (word in msg.lower() for word in d_m.sad_words):
      await message.channel.send(random.choice(encouragements))

    # This will send a random haiku from the database
    if msg.startswith("haiku"):
      await message.channel.send(random.choice(poems))

  # this will allow a user to add a new encouraging message
  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    d_m.create_encouragement(encouraging_message)
    await message.channel.send("New encouraging message added.")

  # This allows a user to delete an encouraging message
  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del", 1)[1])
      d_m.delete_encouragement(index)
      encouragements = db["encouragements"]

    await message.channel.send(encouragements)

  # This lists all encouraging messages
  if msg.startswith("$list"):
    encouragements = []
    output = ""

    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    for i in encouragements:
      output += f'{encouragements.index(i)}: {i} \n'

    await message.channel.send('---Encouragements---\n' + output)


  if msg.startswith("$responding"):
    value = msg.split("$responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send('Responding is active.')
    else:
      db["responding"] = False 
      await message.channel.send('Responding is disabled.')


  if msg.startswith("notice me senpai"):
    await message.channel.send("I notice you " + friend + ", but you would be better seen not heard.")


  if msg.startswith("$help"):
    await message.channel.send(reply.give_help(friend))

  
  if msg.startswith("$haiku"):
    haiku = msg.split("$haiku ",1)[1]
    d_m.create_haiku(haiku)
    await message.channel.send("New haiku added.")


  # This allows a user to delete a haiku
  if msg.startswith("$un haiku)"):
    haikus = []
    if "haikus" in db.keys():
      index = int(msg.split("$un haiku ", 1)[1])
      d_m.delete_haiku(index)
      haikus = db["haikus"]

    await message.channel.send(haikus)


  if msg.startswith("$all haiku"):
    haikus = []
    output = ""
    if "haikus" in db.keys():
      haikus = db["haikus"]

    for i in haikus:
      output += f'{haikus.index(i)}: {i} \n \n'

    await message.channel.send('---Haikus---\n \n' + output)
    

keep_alive()
client.run(discord_token)
