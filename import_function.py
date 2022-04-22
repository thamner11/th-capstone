import sqlite3
import csv

connection = sqlite3.connect('capstone.db')

cursor = connection.cursor()

def import_csv():
    list = []

    with open('csv_file.csv', 'r') as csvfile:
        data = csv.reader(csvfile)
        headerrow = next(data)
        query = "INSERT INTO Assessment_Results (user_id, assessment, score, date_taken, time_taken) VALUES (?, ?, ?, ?, ?)"
        
        if headerrow != None:
            for row in data:
                list.append(row)
                print(list)

        cursor.executemany(query, list)

        connection.commit()

