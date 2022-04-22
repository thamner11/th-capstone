import sqlite3
import bcrypt

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()


def add_user(): #working!!!!working!!!!working!!!!
  
    print('\n~~~~~Add a User to the Dream Team~~~~~\n')
    first_name = input('Please enter a first name: ')
    last_name = input('Please enter a last name: ')
    phone = input('Please enter their phone number: ')
    email = input('Please enter their email: ')
    password = input('Please enter a password for the user: ')

    date_created = input('Please enter the date this was created: ')
    hire_date = input('Please enter their hire date: ')
    user_type = input('Are you a Manager (Yes or No): ')
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    query = "INSERT INTO Users (first_name, last_name, phone, email, password, date_created, hire_date, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    values = [first_name, last_name, phone, email, hashed, date_created, hire_date, user_type]
   
    cursor.execute(query, values)
    connection.commit()

def add_new_competency():#working!!!!working!!!!working!!!!
    print('\n~~~~~Add a new competency to the Dream Team~~~~~\n')
    name = input('Please enter the name of the competency: ')
    date_created = input('Please enter the date this was created: ')

    query = "INSERT INTO Competencies (name, date_created) VALUES (?, ?)"
    values = [name,  date_created]
   
    cursor.execute(query, values)
    connection.commit()


def add_assessments(): #working!!!!working!!!!working!!!!
    print('\n~~~~~Add a new assessment to a competency to the Dream Team~~~~~\n')
    name = input('Please enter the name of the new assessment: ')
    competency = input('Please enter the Competency related to this Assessment: ')
    date_created = input('Please enter the date this was created: ')


    query = "INSERT INTO Assessments (name, competency, date_created) VALUES (?, ?, ?)"
    Values = [name, competency, date_created, ]
   
    cursor.execute(query, Values)
    connection.commit()



def add_assessment_results(): #working!!!!working!!!!working!!!!
    print('\n~~~~~Add the assessment results to one of the Dream Team members~~~~~\n')
    user_id = input('Please enter the user id of the person you are scoring: ')
    assessment = input('Please enter the assessment name: ')
    score = input('Please enter their score between 0 and 4: ')
    date_taken = input('Please enter the date this assessment was taken: ')
    time_taken = input('Please enter the time the member took the assessment: ')
   

    query = "INSERT INTO Assessment_Results (user_id, assessment, score, date_taken, time_taken) VALUES (?, ?, ?, ?, ?)"
    Values = [user_id, assessment, score, date_taken, time_taken]
   
    cursor.execute(query, Values)
    connection.commit()