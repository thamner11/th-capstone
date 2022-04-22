import sqlite3
import csv

connection = sqlite3.connect('capstone.db')

cursor = connection.cursor()

def manager_export():
    lines = cursor.execute("SELECT * FROM Users").fetchall()
    with open('capstone.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['User ID', 'First Name', 'Last Name', 'Phone Number', 'Email', 'Password', 'Active', 'Date Created', 'Hire Date', 'User Type'])
        writer.writerows(lines)
        







