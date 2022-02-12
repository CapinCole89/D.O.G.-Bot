import discord
import os
from keep_alive import keep_alive
from message_handler import message_handler


def paragraph_case(string):
  string = '. '.join(i.capitalize() for i in string.split('. '))


def main():
  discord_token = os.environ['Token']
  client = discord.Client()


  # This initialises the bot and returns a confirmation in the terminal
  @client.event
  async def on_ready():
    print('We have logged in as {0.user}'.format(client))

  # This initialises when a message comes into the server
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    bot_response = message_handler(message)

    if bot_response:
      await message.channel.send(bot_response)
    

  keep_alive()
  client.run(discord_token)


if __name__ == '__main__':
  main()
