import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def delete_result(user_id):
    results = f'DELETE FROM Assessment_Results WHERE user_id={user_id}'
    cursor.execute(results)