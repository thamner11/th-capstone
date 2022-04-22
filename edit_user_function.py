import sqlite3

from view_function import view_members
from tkinter import *
connection = sqlite3.connect('capstone.db')

cursor = connection.cursor()




def update_userperson(update_user):
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome~~~~~~~~~~~~~~~~~~~~~~\n')
    print('\n\n~~~~~~~We appreciate your time at the Dream Team~~~~~~~\n')
    while True:
                    user_view = input( '\n\nWhat would you like to update?  \n\n[A] Edit a Users First Name\n[B] Edit a Users Last Name \n[C] Edit a Competency Date\n[D] Edit a Competency Name \n[E] Edit an Assessment date\n[F] Edit an Assessment name\n[G] Edit an Competency of the Assessment\n[H] Edit an Assessment Result\n[R] Return to Main Menu\n\n' )

                    if user_view == 'A':  # update_person(update_user)
                        print ('~~~~~~Edit your first name~~~~~~~')
                        
                        update_value = input("Enter the updated first name: \n") 
                        query = f"UPDATE Users SET first_name = ? WHERE user_id = {update_user}"
                        cursor.execute(query, [user_view]) 
                        connection.commit() #has to be above answer for it to print in database.  


                    elif user_view == 'B':  # update_person(update_user)
                        print ('~~~~~~Edit your last name~~~~~~~')
                        
                        update_value = input("Enter the updated last name: \n") 
                        query = f"UPDATE Users SET last_name = ? WHERE user_id = {update_user}"
                        cursor.execute(query, [update_value]) 
                        connection.commit() #has to be above answer for it to print in database.  

                    elif user_view == 'C':
                        print ('~~~~~~Edit your Phone~~~~~~~')
                        update_value = input("Enter the updated phone number: \n") 
                        query = f"UPDATE Users SET phone = ? WHERE user_id = {update_user}"
                        cursor.execute(query, [update_value]) 
                        connection.commit()

                    elif user_view == 'D':
                        print ('~~~~~~Edit your Email~~~~~~~')
                        update_value = input("Enter the updated email: \n") 
                        query = f"UPDATE Users SET email = ? WHERE user_id = {update_user}"
                        cursor.execute(query, [update_value]) 
                        connection.commit()

                    elif user_view == 'E':
                        print ('~~~~~~Edit your Password~~~~~~~')
                        user_view = input('Please enter your new password')
                        
                        query = f"UPDATE Users SET password = ? WHERE user_id = {update_user}"
                        cursor.execute(query, [update_value]) 
                        connection.commit()

                    elif user_view == 'R':
                        break
                    update_value = ['']
                    query = ''
connection.commit()
