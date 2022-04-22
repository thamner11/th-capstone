import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def activate_user(user_id):
    user_update = f'ACTIVATE FROM Assessment_Results WHERE user_id={user_id}'
    cursor.execute(results)