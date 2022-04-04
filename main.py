# Assignment Nro 2. Python DB and File
# Name: Martha Tellez
# Student ID: 8746962


import csv
import sqlite3


start=True
while start:
    print("************************************************")
    print("**************LOGIN MODULE**********************")
    print("************************************************\n")
    print("\n***************ENTER INFORMATION**************\n (1) Create User \n", "(2) Manage Places\n",
          "(3) Booking\n","(4) Reports \n", " (5) Quit Application\n")

    codes1 = []
    codes2 = []


    # Create connection with DB, and insert in to the table

    connection = sqlite3.connect("Travel_Agency.db")
    newpassword = ''
    option = input("Select the Option:")
    option = int (option)
    if option == 1:
        account=0
        resultsUserCreated = None

        print("\n***************TYPE OF USER**************\n (1) Admin User \n", "(2) Normal User\n")

        optionUser = input("Select the Option:")
        optionUser = int(optionUser)

        if optionUser==1:
            print("\n**********************************************")
            print("*************CREATE ADMIN USER******************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password (Letters and Numbers): \n")
            password = password.upper()
            firstName = input("Enter your First Name): \n")
            firstName = firstName.upper()
            lastName = input("Enter your Last Name): \n")
            lastName = lastName.upper()
            phone = input("Enter your Phone Number): \n")
            phone = phone.upper()

            # Qry User and Nro times to access
            # ---------------------------------------------------------------------------------------------
            cursor = connection.cursor()
            cursor.execute(
            "SELECT UserName FROM User WHERE UserType =  '0'")
            resultsUserCreated = cursor.fetchone()
            cursor.close()

            if resultsUserCreated == None:
                # Create connection with DB, and insert in to the table

                connection = sqlite3.connect("Travel_Agency.db")
                # --------------------------------------------------------------------------------
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO User (UserName, Password, FirstName, LastName, Phone, UserType ) values ('" + email + "','" + password + "','" + firstName + "','" + lastName + "','" + phone + "','0');")
                cursor.execute("COMMIT;")
                cursor.close()
                # --------------------------------------------------------------------------------
                connection.close()
                print("\nThe user was successfully created\n")
            else:
                print("\nThe Admin user already exists\n")

        if optionUser == 2:
            print("\n**********************************************")
            print("*************CREATE NORMAL USER************************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password (Letters and Numbers): \n")
            password= password.upper()
            firstName = input("Enter your First Name): \n")
            firstName = firstName.upper()
            lastName = input("Enter your Last Name): \n")
            lastName = lastName.upper()
            phone = input("Enter your Phone Number): \n")
            phone = phone.upper()

            # Qry User and Nro times to access
            # ---------------------------------------------------------------------------------------------
            cursor = connection.cursor()
            cursor.execute(
                "SELECT UserName FROM User WHERE UserName = '" + email + "' and  (UserType =  '0' or UserType = '1')")
            resultsUserCreated = cursor.fetchone()
            cursor.close()

            if resultsUserCreated == None:
                # --------------------------------------------------------------------------------
                cursor = connection.cursor()
                cursor.execute("INSERT INTO User (UserName, Password, FirstName, LastName, Phone ) values ('"+email+"','"+password+"','"+firstName+"','"+lastName+"','"+phone+"');")
                cursor.execute("COMMIT;")
                cursor.close()
                # --------------------------------------------------------------------------------
                connection.close()
                print("\nThe user was successfully created\n")
            else:
                print("\nThe user already exists\n")

    elif option == 2:
            count = ''
            print("\n**********************************************")
            print("*************MANAGE PLACES**********************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password: \n")
            password = password.upper()

            connection = sqlite3.connect("Travel_Agency.db")
            # --------------------------------------------------------------------------------
            cursor = connection.cursor()
            cursor.execute("SELECT ACCESS_COUNT FROM TRAVEL_AGENCY WHERE LOGIN = '"+email+"' AND CRYPTOGRAPHIC_PASSWORD = '"+newpassword+"'")
            count = cursor.fetchone()
            #access = type(int(count[0]))+ 1
            if(count != None):
                for i in range(len(count)):
                    access = count[i]
                    access = access + 1
                cursor.close()
                # --------------------------------------------------------------------------------

            # update times to access in database
               # cursor = connection.cursor()
                #cursor.execute(
                 #   "UPDATE TB_USER SET ACCESS_COUNT = "+str(access)+" WHERE LOGIN = '"+email+"' AND CRYPTOGRAPHIC_PASSWORD = '"+newpassword+"';")
                # cursor.execute("COMMIT;")
                # cursor.close()
            # Qry User and Nro times to access
                #---------------------------------------------------------------------------------------------
                # cursor = connection.cursor()
                # cursor.execute(
                  #  "SELECT LOGIN, ACCESS_COUNT FROM TB_USER WHERE LOGIN = '" + email + "' AND CRYPTOGRAPHIC_PASSWORD = '" + newpassword + "'")
                # results1 = cursor.fetchall()
                # cursor.close()

            # Qry all Data to backup file
                #-------------------------------------------------------------------------------------------------------------
               # cursor = connection.cursor()
                #cursor.execute(
                 #   "SELECT * FROM TB_USER ")
                #results2 = cursor.fetchall()
                # cursor.close()

                # for i in range(len(results1)):
                  #  print("\nSuccessful Access, Your User and Login Number is:"+ str(results1[i])+"\n")
                # --------------------------------------------------------------------------------
                #connection.close()
            # Write backup file
                #file_backup = open('userdb-backup.csv', mode='w')

                # Write file operation
                #for i in range(len(results2)):
                    #file_backup.write(str(results2[i])+"\n")

                #file_backup.close()

            else:
                print("\n The user or password is not correct try again, please \n")

    elif option == 3:
            count = ''
            print("\n**********************************************")
            print("*******************BOOKING**********************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password: \n")
            password = password.upper()
    elif option == 4:
            count = ''
            print("\n**********************************************")
            print("*******************REPORTS**********************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password: \n")
            password = password.upper()


    elif option == 5:
        start = False


