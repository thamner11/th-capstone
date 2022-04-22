import sqlite3
# from new_login_function import newlogin, user_manager
import bcrypt
from import_function import import_csv
# from tkinter import *

from export import manager_export
from search import search_user

from add_function import add_user, add_new_competency, add_assessments, add_assessment_results
from import_function import import_csv
from delete_function import delete_result
from edit_function import update_person
from view_function import view_members, view_user_competencies, admin_view_scores

connection = sqlite3.connect('capstone.db')

cursor = connection.cursor()
def mangmenu():
    print('\n\n~~~~~~~Welcome Manager~~~~~~~\n')
    print('\n\n~~~~~~~We appreciate your time at the Dream Team~~~~~~~\n')
    while True:
        
        user = input('Please choose from the following options: \n\n [1] View database\n\n [2] Search for a certain Person \n\n [3] Add information to the database\n\n [4] Delete an assessment result\n\n [5] Edit database \n\n [6] Import assessment results\n\n [7] Export assessment results\n\n [Q] Quit \n\n')

        if user == '1':
    
            print('\n~~~~~View the Database~~~~~\n')
            while True:
                manager_view = input( '\n\nWhat would you like to view?  \n\n[A] View Users of the Dream Team\n[B] Search for a certain Person\n[C] View all user competencies by User ID\n[D] View a report of all users and their competency levels for a given competency\n[R]Return to Main Menu\n\n' )

                if manager_view == 'A':
                    print ('~~~~~~Dream Team~~~~~~~')
                    view_members()
                elif manager_view == 'B':
                    print ('~~~~~~Search the Dream Team~~~~~~~')
                    search_user()
                elif manager_view == 'C':
                    print ('~~~~~~View all Dream Team user competencies~~~~~~~')
                    assessment = input('Please enter an assessment name: \n')
                    view_user_competencies(assessment)

                elif manager_view == 'D':
                    print ('~~~~~~View the Dream Team report of all users and their competency levels for a given competency~~~~~~~')
                    user_id = input('Please enter a user id: \n')
                    admin_view_scores(user_id)
                  
        
                  
                elif manager_view == 'R':
                    break

        elif user == '2': 
            print ('~~~~~~Search the Dream Team~~~~~~~')
            search_user()
            
        elif user == '3':
            print ('~~~~~~Add information to the Dream Team Database~~~~~~~')
            while True:
                manager_view = input( '\n\nWhat would you like to add?  \n\n[A] Add a User to the Dream Team\n[B] Add a new Competency \n[C] Add a New Assessment to a Competency\n[D] Add an Assessment result for a User for an Assessment \n[R]Return to Main Menu\n\n' )

                if manager_view == 'A':
                    print ('~~~~~~Add a New Member to the Dream Team~~~~~~~')
                    add_user()
                elif manager_view == 'B':
                    print ('~~~~~~Add a new Competency~~~~~~~')
                    add_new_competency()
                elif manager_view == 'C':
                    print ('~~~~~~Add a New Assessment to a Competency~~~~~~~')
                    add_assessments()
                elif manager_view == 'D':
                    print ('~~~~~~Add an Assessment result for a User for an Assessment~~~~~~~')
                    add_assessment_results()
                                    
                elif manager_view == 'R':
                    break


        elif user == '4':  #delete an
            delete_id = input("Please enter the assessment name that you need to remove from the database: \n ")
            delete_result(delete_id)
        

        elif user == '5': #edit/update
            print ('~~~~~~How would you like to update the Dream Teams Database~~~~~~~')
            update_user = input('Which person would you like to update: \n\n')
            update_person(update_user)


        elif user == '6':
            print ('~~~~~~Import Assessment Results~~~~~~~')
            import_csv()

        elif user == '7':
            print ('~~~~~~Export Assessment Results~~~~~~~')
            manager_export()

        if user == 'Q':
            print("I hope you saw everything you need to see about your coworkers and clients. If anything you notice is wrong, please let me know.")
            break

        connection.commit()
    # elif main_menu == '2':
    #     create_account()
    #     user_type = user
    #     while user_type == '2':
