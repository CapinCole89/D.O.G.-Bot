from replit import db


sad_words = [
    "sad",
    "depressed",
    'unhappy',
    'miserable',
    'depressing',
    'trash',
    'garbage',
    'i suck',
    "lonely",
]


if db['sad words']:
    sad_words = db['sad words']


def create_entry(msg, table_name):
    # This add an entry to a table, and create the table if it does not exist
    new_entry = msg.split(f'new {table_name} ', 1)[1]

    if table_name in db.keys():
        table_list = db[table_name]
        table_list.append(new_entry)
        db[table_name] = table_list
    else:
        db[table_name] = table_list

    return f'New entry added to {table_name}'


def delete_entry(msg, table_name):
    # This will delete an entry from an existing table
    index = int(msg.split(f'delete {table_name[0:-1]}'))
    table_list = db[table_name]
    if len(table_list) >= index:
        del table_list[index]
        db[table_name] = table_list

    return f'Entry {index} was removed from {table_name}'
