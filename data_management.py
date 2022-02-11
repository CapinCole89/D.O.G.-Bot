from replit import db


def create_entry(msg, table_name):
    # This add an entry to a table, and create the table if it does not exist
    new_entry = msg.split(f'$add {table_name[:-1]}', 1)[1]

    if table_name in db.keys():
        table_list = db[table_name]
        table_list.append(new_entry)
        db[table_name] = table_list
    else:
        db[table_name] = [new_entry]

    return f'New entry added to {table_name}'


def delete_entry(msg, table_name):
    # This will delete an entry from an existing table
    index = int(msg.split(f'$del {table_name[:-1]}', 1)[1])
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
        output += f'{table_list.index(i)}: {i} \n'

    return f'---{table_name}--- \n\n {output}'
