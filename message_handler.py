from message_responses import give_encouragement, give_help, toggle_responses, give_inspiration, list_table, notice
from data_management import create_entry, delete_entry, sad_words


def handle_response(message):
    msg = message.content.lower()
    author = str(message.author)
    friend = author[0: -5]

    async def reply(string):
        await message.channel.send(string)

    if msg.startswith('$help'):
        return give_help(friend)

    elif msg.startswith('$responding'):
        return toggle_responses(msg)

    elif msg.startswith('$inspire'):
        return give_inspiration()

    elif msg.startswith('$new encouragement'):
        return create_entry(msg, 'encouragements')

    elif msg.startswith('$delete encouragement'):
        return delete_entry(msg, 'encouragements')

    elif msg.startswith('$all encouragement'):
        return list_table('encouragements')

    elif msg.startswith('$new haiku'):
        return create_entry(msg, 'haikus')

    elif msg.startswith('$delete haiku'):
        return delete_entry(msg, 'haikus')

    elif msg.startswith('$all haiku'):
        return list_table('haikus')

    elif msg.startswith('notice me senpai'):
        return notice(friend)

    # This will see is a message contains a sad word, then responds
    elif any(word in msg for word in sad_words):
        return give_encouragement()
    
    else:
        pass
