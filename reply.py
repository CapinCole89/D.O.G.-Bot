import requests
import json


def give_help(friend):
  return (
    f"Hi {friend}! I'm the Digitizer of Goals bot, but most call me D.o.G. bot for short. \n"
    "If you would like to hear a haiku simply say haiku. \n"
    "You can add $ before a command, and I'll handle the rest. Here's a list of current commands. \n"
    "$inspire | I will give you a random inspiring quote. \n"
    "$list | This will show you the current list of encouraging words I have for you. \n"
    "$new | This will allow you to add a new encouraging phrase to my database. \n"
    "$del | This will let you delete an encouraging phrase from the system using it's index. \n"
    "$haiku | This will add a new haiku to the database \n"
    "$un haiku | This will let you delete a haiku from the system using it's index. \n"
    "$all haikus | This will return a list all off of the currently stored haikus. \n"
    "Have fun, and don't let yourself go hollow!"
    )


# This function uses an api to get an inspirational quote
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)