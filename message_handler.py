from replit import db
from data_management import create_entry, delete_entry, list_table, sad_words, retrieve_entry
from message_responses import give_encouragement, give_help, toggle_responses, \
    give_inspiration, give_notice, give_haiku


def message_handler(message):
    msg = message.content.lower()
    author = str(message.author)
    friend = author[0: -5]

    # This triggers the help function
    if msg.startswith('$help'):
        return give_help(friend)

    # This goggles the static responses
    if msg.startswith('$responding'):
        return toggle_responses(msg)

    # This gives an inspirational quote
    if msg.startswith('$inspire'):
        return give_inspiration()

    # This will add a new encouragement to the database
    if msg.startswith('$add encouragement'):
        return create_entry(msg, 'encouragements')

    # This will delete an encouragement from the database
    if msg.startswith('$del encouragement'):
        return delete_entry(msg, 'encouragements')

    # This will list all encouragements in the database
    if msg.startswith('$all encouragement'):
        return list_table('encouragements')

    # This will add a new haiku to the database
    if msg.startswith('$add haiku'):
        return create_entry(msg, 'haikus')

    # This will delete an haiku from the database
    if msg.startswith('$del haiku'):
        return delete_entry(msg, 'haikus')

    # This will list all haikus in the database
    if msg.startswith('$all haiku'):
        return list_table('haikus')

    # This will get a specified haiku from the database
    if msg.startswith('$get haiku'):
        return retrieve_entry(msg, 'haikus')

    # This will add a new word to the database
    if msg.startswith('$add sad word'):
        return create_entry(msg, 'sad words')

    # This will delete a sad word from the database
    if msg.startswith('$del sad word'):
        return delete_entry(msg, 'sad words')

    # This will list all sad words in the database
    if msg.startswith('$all sad word'):
        return list_table('sad words')

    # These only trigger if responding is set to true
    if db['responding']:
        # This will ignore commands
        if '$' in msg:
            return

        # This will see is a message contains a sad word, then responds
        if any(word in msg for word in sad_words):
            return give_encouragement()

        # This is a silly easter egg for the anime fans
        if 'notice me senpai' in msg:
            return give_notice(friend)

        # This will give 1 random haiku
        if ('haiku' in msg):
            return give_haiku()
