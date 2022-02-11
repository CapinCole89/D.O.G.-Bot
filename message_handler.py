import random
from replit import db
from message_responses import give_encouragement, give_help, toggle_responses, give_inspiration, list_table, notice
from data_management import create_entry, delete_entry, sad_words


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

    # This will see is a message contains a sad word, then responds
    if any(word in msg.lower() for word in sad_words):
        await reply(give_encouragement())
