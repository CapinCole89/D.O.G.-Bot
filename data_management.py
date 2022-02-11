from ast import Pass
from replit import db


def create_entry(new_entry, table_name):
    # This add an entry to a table, and create the table if it does not exist
    if table_name in db.keys():
        table_list = db[table_name]
        table_list.append(new_entry)
        db[table_name] = table_list
    else:
        db[table_name] = [new_entry]

    return f'New entry added to {table_name}'


def delete_entry(msg, table_name):
    # This will delete an entry from an existing table
    index = int(msg.split(f'$del {table_name[:-1]} ', 1)[1])
    table_list = db[table_name]
    if len(table_list) >= index:
        del table_list[index]
        db[table_name] = table_list

    return f'Entry {index} was removed from {table_name}'


def list_table(table_name):
    # This will list all entries in a specific table
    table_list = []
    output = ''

    if table_name in db.keys():
        table_list = db[table_name]
    else:
        return(f'{table_name} not in database.')

    for i in table_list:
        output += f'{table_list.index(i)}: {i} \n\n'

    return f'---{table_name}--- \n\n {output}'


def retrieve_entry(index, table_name):
    # This will retrive a specific entry from the specified table
    return db[table_name][index]


def update_entry(msg, table_name):
    # This will update a specific entry from the specified table
    index = int(msg.split(' ')[3])
    new_entry = msg.split(index, 1)[1]
    db[table_name][index] = new_entry

    return db[table_name][index]



sad_words = db['sad words']
