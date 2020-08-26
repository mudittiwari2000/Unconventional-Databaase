import sqlite3 as sq

# Show all the records of all table


def showAll():
    conn = sq.connect('customer.db')

    cur = conn.cursor()

    cur.execute('SELECT rowid, * FROM customers')

    items = cur.fetchall()

    for item in items:
        print(f'{item[0]})', item[1], item[2], item[3])

    conn.commit()

    conn.close()

# Add a new record to the table


def addOne(first, last, email):
    conn = sq.connect('customer.db')
    cur = conn.cursor()
    cur.execute('''

        INSERT INTO customers VALUES(?, ?, ?)

    ''', (first, last, email))
    conn.commit()
    conn.close()

# Add many records to the table


def addMany(recordList):
    conn = sq.connect('customer.db')
    cur = conn.cursor()

    cur.executemany('''

        INSERT INTO customers VALUES(?, ?, ?)

    ''', recordList)

    # Commit and close
    conn.commit()
    conn.close()

# Delete record from table


def deleteOne(id):
    conn = sq.connect('customer.db')
    cur = conn.cursor()

    # Here the passed parameter needs to be converted into a tuple or a list
    cur.execute('''

        DELETE FROM customers WHERE rowid = (?)

    ''', (id, ))

    # Commit and close
    conn.commit()
    conn.close()

# Lookup with WHERE


def lookUpByEmail(email):
    conn = sq.connect('customer.db')
    cur = conn.cursor()

    cur.execute('''

    SELECT * FROM customers WHERE email = (?)

    ''', (email, ))

    yield cur.fetchone()

    # Commit and close
    conn.commit()
    conn.close()
