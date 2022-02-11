from turtle import up
from replit import db
from data_management import create_entry, delete_entry, list_table, sad_words, retrieve_entry, update_entry
from message_responses import give_encouragement, give_help, toggle_responses, \
    give_inspiration, give_notice, give_haiku


def message_handler(message):
    msg = message.content.lower()
    author = str(message.author)
    friend = author[0: -5]
    command = ''
    table_name = ''
    value = ''

    tables = ['haikus', 'sad words', 'encouragements']

    if msg.startswith('$'):
        command = msg.split(' ', 1)[0]
        value = msg.split(' ', 1)[1]

        for title in tables:
            if value.startswith(title):
                table_name = title
                value = value.split(f'{table_name} ', 1)[1]

    # This will list all values stored in the specified table
    if command == '$all':
        return list_table(table_name)

    # This will retrive a specific value stored in the specified table
    if command == '$get':
        return retrieve_entry(value, table_name)

    # This will add an entry to the specified table
    if command == '$add':
        return create_entry(value, table_name)

    # This will update an entry in the specified table
    if command == '$edit':
        return update_entry(msg, table_name)

    # This will delete an entry from the specified table
    if command == '$del':
        return delete_entry(msg, table_name)

    # This triggers the help function
    if command == '$help':
        return give_help(friend)

    # This goggles the static responses
    if command == '$responding':
        return toggle_responses(message)

    # This gives an inspirational quote
    if command == '$inspire':
        return give_inspiration()


    # These only trigger if responding is set to true
    if db['responding']:
        # This will ignore commands
        if msg.startswith('$'):
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
