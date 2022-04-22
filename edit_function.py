import sqlite3

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

def update_person(update_user): 
    while True:
        manager_view = input( '\n\nWhat would you like to update?  \n\n[A] Edit a Users First Name\n[B] Edit a Users Last Name \n[C] Edit a Competency Date\n[D] Edit a Competency Name \n[E] Edit an Assessment date\n[F] Edit an Assessment name\n[G] Edit an Competency of the Assessment\n[H] Edit an Assessment Result\n[R] Return to Main Menu\n\n' )

        if manager_view == 'A':  # update_person(update_user)
            print ('~~~~~~Edit a Dream Team User~~~~~~~')
            update_user = input('Which person would you like to update enter user_id: \n\n')
            update_value = input("Enter the updated first name: \n") 
            query = f"UPDATE Users SET first_name = ? WHERE user_id = {update_user}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which person would you like to update user_id: \n\n ')
                update_person(update_user)
            if answer == "n":
                return

        if manager_view == 'B':  # update_person(update_user)
            print ('~~~~~~Edit a Dream Team User~~~~~~~')
            update_user = input('Which person would you like to update enter user_id: \n\n')
            update_value = input("Enter the updated last name: \n") 
            query = f"UPDATE Users SET last_name = ? WHERE user_id = {update_user}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which person would you like to update enter user_id: \n\n ')
                update_person(update_user)
            if answer == "n":
                return

        elif manager_view == 'C':
            print ('~~~~~~Edit a Competency~~~~~~~')
            
            update_competency = input('Which Competency would you like to update: \n\n')
            update_value = input("Enter the name of the Competency: \n") 
            query = f"UPDATE Competencies SET date_created = ? WHERE user_id = {update_competency}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which competency would you like to update: \n\n ')
                update_person(update_competency)
            if answer == "n":
                return
        elif manager_view == 'D':
            print ('~~~~~~Edit a Competency~~~~~~~')
            
            update_competency = input('Which Competency would you like to update: \n\n')
            update_value = input("Enter the name of the Competency: \n") 
            query = f"UPDATE Competencies SET name = ? WHERE user_id = {update_competency}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which competency would you like to update: \n\n ')
                update_person(update_competency)
            if answer == "n":
                return

        elif manager_view == 'E':
            print ('~~~~~~Edit an Assessment~~~~~~~')
            
            update_competency = input('Which Assessment would you like to update: \n\n')
            update_value = input("Enter the name of the Assessment: \n") 
            query = f"UPDATE Assessments SET date_created = ? WHERE user_id = {update_competency}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which Assessment would you like to update: \n\n ')
                update_person(update_competency)
            if answer == "n":
                return
        elif manager_view == 'F':
            print ('~~~~~~Edit an Assessment~~~~~~~')
            
            update_competency = input('Which Assessment would you like to update: \n\n')
            update_value = input("Enter the name of the Assessment: \n") 
            query = f"UPDATE Assessments SET name = ? WHERE user_id = {update_competency}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which Assessment would you like to update: \n\n ')
                update_person(update_competency)
            if answer == "n":
                return
        elif manager_view == 'G':
            print ('~~~~~~Edit an Assessment~~~~~~~')
            update_competency = input('Which Assessment would you like to update: \n\n')
            update_value = input("Enter the competency of the Assessment: \n") 
            query = f"UPDATE Assessments SET competency = ? WHERE user_id = {update_competency}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which Assessment would you like to update: \n\n ')
                update_person(update_competency)
            if answer == "n":
                return            


        elif manager_view == 'H':
            print ('~~~~~~Edit an Assessment Result~~~~~~~')
            update_competency = input('Which Assessment Result would you like to update: \n\n')
            update_value = input("Enter the name of the user: \n") 
            query = f"UPDATE Assessments SET name = ? WHERE user_id = {update_competency}"
            cursor.execute(query, [update_value]) 
            connection.commit() #has to be above answer for it to print in database.  
            answer = input("Update another item? (y/n)  ")
                            
            if answer == "y":
                update_user = input('Which Assessment Result would you like to update: \n\n ')
                update_person(update_competency)
            if answer == "n":
                return        
        elif manager_view == 'R':
            break
        update_value = ['']
        query = ''
    

connection.commit()
   