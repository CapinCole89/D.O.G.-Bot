import requests
import json
from replit import db
from data_management import create_entry, delete_entry


def give_help(friend):
    return (
        f"Hi {friend}! I'm the Digitizer of Goals bot, but most call me D.o.G. bot for short. \n\n"
        "If you would like to hear a haiku simply say haiku. \n\n"
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
def give_inspiration():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)


def toggle_responses(msg):
    value = msg.split("$responding ", 1)[1]

    if "responding" not in db.keys():
        db["responding"] = True

    if value.lower() == "false":
        db["responding"] = False
        return 'Responding is disabled.'
    else:
        db["responding"] = True
        return 'Responding is active.'


def notice(friend):
    return f"I notice you {friend}, but you would be better seen not heard."


def list_table(table_name):
    table_list = []
    output = ''

    if table_name in db.keys():
        table_list = db[table_name]
    else:
        return(f'{table_name} not in database.')

    for i in table_list:
        output += f'{table_list.index(i)}: {i} \n'

    return f'---{table_name}--- \n\n {output}'


async def handle_response(message):
    msg = message.content.lower()
    author = str(message.author)
    friend = author[0: -5]

    async def reply(string):
        await message.channel.send(string)

    if msg.startswith('$help'):
        await reply(give_help(friend))

    if msg.startswith('$responding'):
        await reply(toggle_responses(msg))

    if msg.startswith('$inspire'):
        await reply(give_inspiration())

    if msg.startswith('$new encouragement'):
        await reply(create_entry(msg, 'encouragements'))

    if msg.startswith('$delete encouragement'):
        await reply(delete_entry(msg, 'encouragements'))

    if msg.startswith('$all encouragement'):
        await reply(list_table('encouragements'))

    if msg.startswith('$new haiku'):
        await reply(create_entry(msg, 'haikus'))

    if msg.startswith('$delete haiku'):
        await reply(delete_entry(msg, 'haikus'))

    if msg.startswith('$all haiku'):
        await reply(list_table('haikus'))

    if msg.find('notice me senpai'):
        await reply(notice(friend))
