import sqlite3

DATABALE_NAME = 'testdb.db'

def create_table():
    con = sqlite3.connect(DATABALE_NAME)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE user (id INTEGER, username TEXT, password TEXT, PRIMARY KEY(id))")
    cursor.execute("INSERT INTO user (id,username, password) VALUES (1, 'homer', '2aaab795b3836904f82efc6ca2285d927aed75206214e1da383418eb90c9052f')")
    cursor.execute("INSERT INTO user (id,username, password) VALUES (2, 'marge', 'b4b811fa40505329ae871e52f03527c3720c9af7fb8607819658535c5484c41e')")
    cursor.execute("INSERT INTO user (id,username, password) VALUES (3, 'bart', '9551dadbf76a27457946e70d1aebebe2132f8d3bce6378d216c11853524dd3a6')")
    cursor.execute("INSERT INTO user (id,username, password) VALUES (4, 'lisa', 'd84fe7e07bedb227cffff10009151d96fc944f6a1bd37cff60e8e4626a1eb1c3')")
    cursor.execute("INSERT INTO user (id,username, password) VALUES (5, 'maggie', 'aae5be5f6474904b686f639e0fcfd2be440121cd889fa381a94b71750758345e')")
    con.commit()
    con.close()

def select_users():
    conn = sqlite3.connect(DATABALE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * from user')
    table = cursor.fetchall()
    for row in table:
        print(row)
    conn.close()

def select_users_starting_with(prefix):
    conn = sqlite3.connect(DATABALE_NAME)
    cursor = conn.cursor()
    parameters = (prefix,)
    cursor.execute("SELECT * from user WHERE username LIKE ?", parameters)
    table = cursor.fetchall()
    for row in table:
        print(row)
    conn.close()

def drop_table():
    conn = sqlite3.connect(DATABALE_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE user")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    #select_users()
    select_users_starting_with("m%")
    drop_table()
