import sqlite3

lines = []
connection = sqlite3.connect("restored-employees.db")
connection.execute("CREATE TABLE IF NOT EXISTS employees (name VARCHAR, age INTEGER, duty VARCHAR)")
connection.commit()


def insert(conn, params):
    print("Inserting: %s"%params)
    conn.execute("INSERT INTO employees(name, age, duty) values(?, ?, ?)", params)

def update(conn, params):
    print("Update: %s"%params)
    conn.execute("UPDATE employees SET %s=? WHERE name=?"%params[1], (params[2], params[0]))

def delete(conn, params):
    print("Delete: %s"%params)
    conn.execute("DELETE FROM employees WHERE name=?", params)

with open('backup.log', 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
for line in lines:
    split_list = line.split(": ")
    method = split_list[0]
    params = split_list[1].split(", ")
    if method == "INSERT":
        insert(connection, params)
    elif method == "UPDATE":
        update(connection, params)
    elif method == "DELETE":
        delete(connection, params)
items = [line for line in connection.execute("SELECT * FROM employees")]
print("ITEMS: %s"%items)
