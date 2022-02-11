import random
import requests
import json
from replit import db


def give_help(friend):
    # This gives a help respone listing all the public bot commands
    return (
        f"Hi {friend}! I'm the Digitizer of Goals bot, but most call me D.o.G. bot for short. \n\n"
        "If you would like to hear a haiku simply say 'haiku'. \n"
        "You can add $ before a command, and I'll handle the rest. Here's a list of current commands. \n"
        "$inspire | I will give you a random inspiring quote. \n"
        "$all encouragements | This will show you the current list of encouraging words I have for you. \n"
        "$add encouragement | This will allow you to add a new encouraging phrase to my database. \n"
        "$del encouragement | This will let you delete an encouraging phrase from the system using it's index. \n"
        "$add haiku | This will add a new haiku to the database \n"
        "$del haiku | This will let you delete a haiku from the system using it's index. \n"
        "$all haikus | This will return a list all off of the currently stored haikus. \n\n"
        "Have fun, and don't let yourself go hollow!"
    )


def give_inspiration():
    # This uses an api to get a random inspirational quote
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']

    return(quote)


def toggle_responses(msg):
    # This will toggle the auto-responses (ones that were not specifically requested)
    value = msg.split("$responding ", 1)[1]

    if "responding" not in db.keys():
        db["responding"] = True

    if value.lower() == "false":
        db["responding"] = False
        return 'Responding is disabled.'
    else:
        db["responding"] = True
        return 'Responding is active.'


def give_notice(friend):
    # This give the anime easter egg
    return f"I notice you {friend}, but you would be better seen not heard."


def list_table(table_name):
    # This will list all entries in a specific table
    table_list = []
    output = ''

    if table_name in db.keys():
        table_list = db[table_name]
    else:
        return(f'{table_name} not in database.')

    for i in table_list:
        output += f'{table_list.index(i)}: {i} \n'

    return f'---{table_name}--- \n\n {output}'


def give_encouragement():
    # This will return a random encouraging saying
    encouragements = db['encouragements']

    return random.choice(encouragements)


def give_haiku():
    # This will return a random haiku
    haikus = db['haikus']

    return random.choice(haikus)
