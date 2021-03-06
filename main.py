# Assignment Nro 2. Python DB and File
# Name: Martha Tellez
# Student ID: 8746962


import csv
import sqlite3
import datetime
#import ax as ax
#import fig as fig
import pandas as pd
import matplotlib.pyplot as plt


start=True
while start:
    print("************************************************")
    print("***********TRAVEL AGENCY SYSTEM*****************")
    print("************************************************\n")
    print("\n***********SELECT MODULE++++++++**************\n (1) Create User \n", "(2) Manage Places\n",
          "(3) Booking\n","(4) Reports \n", "(5) Quit Application\n")

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
            print("*************1. CREATE ADMIN USER****************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password (Letters and Numbers): \n")
            password = password.upper()
            firstName = input("Enter your First Name: \n")
            firstName = firstName.upper()
            lastName = input("Enter your Last Name: \n")
            lastName = lastName.upper()
            phone = input("Enter your Phone Number: \n")
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
            print("*************2. CREATE NORMAL USER***************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password (Letters and Numbers): \n")
            password= password.upper()
            firstName = input("Enter your First Name: \n")
            firstName = firstName.upper()
            lastName = input("Enter your Last Name: \n")
            lastName = lastName.upper()
            phone = input("Enter your Phone Number: \n")
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
            managePlaces = True
            print("\n**********************************************")
            print("**********AUTHENTICATION MODULE******************")
            print("************************************************")

            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password: \n")
            password = password.upper()

            connection = sqlite3.connect("Travel_Agency.db")
            # --------------------------------------------------------------------------------
            cursor = connection.cursor()
            cursor.execute(
                "SELECT UserName FROM User WHERE UserName = '" + email + "' and  UserType =  '0'")
            resultsValidatedAdmin = cursor.fetchone()
            cursor.close()

            if resultsValidatedAdmin != None:
                while(managePlaces):
                    print("\n**********************************************")
                    print("\n***************ADMIN PLACES*******************\n (1) Create Places \n", "(2) View Places\n","(3) Update Places\n","(4) Delete Places\n")
                    print("\n**********************************************")
                    optionPlaces = input("Select the Option:")
                    optionPlaces = int(optionPlaces)


                    if optionPlaces == 1:
                        print("\n**********************************************")
                        print("*************1. CREATE PLACES****************")
                        print("************************************************")

                        descriptionPlace = input("Enter Description Place: \n")
                        descriptionPlace = descriptionPlace.upper()
                        country = input("Enter Country: \n")
                        country= country.upper()
                        price = input("Enter Price: \n")
                        price = price.upper()
                        address = input("Enter Address: \n")
                        address = address.upper()
                        nameContact = input("Enter Name Contact: \n")
                        nameContact = nameContact.upper()
                        phoneContactPlace = input("Enter Phone Contact: \n")
                        phoneContactPlace = phoneContactPlace.upper()
                        availabilityStart = input("Enter Availability Start with format):YYYY-MM-DD \n") #CONFIRME VALIDATION
                        availabilityStart = availabilityStart.upper()
                        availabilityEnd = input("Enter Availability End with format):YYYY-MM-DD \n")  # CONFIRME VALIDATION
                        availabilityEnd = availabilityEnd.upper()

                        # --------------------------------------------------------------------------------
                        cursor = connection.cursor()
                        cursor.execute(
                            "INSERT INTO Place (Description, Country, Price, Address, NameContact,PhoneContact,AvailabilityStart,AvailabilityEnd ) "
                            "values ('" + descriptionPlace + "','" + country + "','" + price + "','" +
                            address + "','" + nameContact + "','" + phoneContactPlace + "','" + availabilityStart + "','" + availabilityEnd + "');")
                        cursor.execute("COMMIT;")
                        cursor.close()
                        # --------------------------------------------------------------------------------
                    print("\nThe place was successfully created\n")

                    if optionPlaces == 2:


                        print("\n**********************************************")
                        print("*************2. VIEW PLACES****************")
                        print("************************************************")
                        # --------------------------------------------------------------------------------
                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT PlaceID FROM Place")
                        resultsPlaceId = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT Description FROM Place")
                        resultsDescription = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT Country FROM Place")
                        resultsCountry = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT Price FROM Place")
                        resultsPrice = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT Address FROM Place")
                        resultsAddress = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT NameContact FROM Place")
                        resultsNameContact = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT PhoneContact FROM Place")
                        resultsPhoneContact = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT AvailabilityStart FROM Place")
                        resultsAvailabilityStart = cursor.fetchall()
                        cursor.close()

                        cursor = connection.cursor()
                        cursor.execute(
                            "SELECT AvailabilityEnd FROM Place")
                        resultsAvailabilityEnd = cursor.fetchall()
                        cursor.close()


                        for i in range(len(resultsPlaceId)):
                            print("\nPlaces: Place ID:" + str(resultsPlaceId[i]) + "\n")
                            print("Description:" + str(resultsDescription[i]) + "\n")
                            print("Country:" + str(resultsCountry[i]) + "\n")
                            print("Price:" + str(resultsPrice[i]) + "\n")
                            print("Address:" + str(resultsAddress[i]) + "\n")
                            print("NameContact:" + str(resultsNameContact[i]) + "\n")
                            print("PhoneContact:" + str(resultsPhoneContact[i]) + "\n")
                            print("AvailabilityStart:" + str(resultsAvailabilityStart[i]) + "\n")
                            print("AvailabilityEnd:" + str(resultsAvailabilityEnd[i]) + "\n")


                            # --------------------------------------------------------------------------------


                    if optionPlaces == 3:
                        print("\n**********************************************")
                        print("*************3. UPDATE PLACES****************")
                        print("************************************************")
                        account = 0

                        print("\n**********************************************")
                        PlaceID = input("Enter Place ID to Update: \n")
                        PlaceID = int(PlaceID)

                        print("\n**********************************************")

                        price = input("Enter Price): \n")
                        price = price.upper()
                        availabilityStart = input("Enter Availability Start with format:YYYY-MM-DD \n")  # CONFIRME VALIDATION
                        availabilityStart = availabilityStart.upper()
                        availabilityEnd = input("Enter Availability End with format:YYYY-MM-DD \n")  # CONFIRME VALIDATION
                        availabilityEnd = availabilityEnd.upper()
                        # update times to access in database
                        cursor = connection.cursor()
                        cursor.execute("UPDATE Place SET  Price = '" + price +  "',AvailabilityStart = '" + availabilityStart + "',AvailabilityEnd = '" + availabilityEnd + "' WHERE PlaceId = " + str(PlaceID) + ";")
                        cursor.execute("COMMIT;")
                        cursor.close()

                        print("\nThe place was successfully updated\n")


                    if optionPlaces == 4:
                        print("\n**********************************************")
                        print("*************4. DELETE PLACES****************")
                        print("************************************************")
                        account = 0

                        print("\n**********************************************")
                        PlaceID = input("Enter Place ID to Delete: \n")
                        PlaceID = int(PlaceID)

                        print("\n**********************************************")

                        cursor = connection.cursor()
                        cursor.execute("DELETE FROM Place WHERE PlaceId = " + str(PlaceID) + ";")
                        cursor.execute("COMMIT;")
                        cursor.close()
                        print("\nThe place was successfully deleted\n")

                    elif optionPlaces == 5:
                        managePlaces = False
            else:
                print("\n The user or password is not correct try again, please \n")

    elif option == 3:
            exit= False
            count = ''
            print("\n**********************************************")
            print("*******************BOOKING**********************")
            print("************************************************")
            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password: \n")
            password = password.upper()

            connection = sqlite3.connect("Travel_Agency.db")
            # --------------------------------------------------------------------------------
            cursor = connection.cursor()
            cursor.execute(
                "SELECT UserID FROM User WHERE UserName = '" + email + "' and  UserType =  '1'")
            resultsValidatedUser = cursor.fetchall()

            characters = "(',)"
            if len(resultsValidatedUser) != 0:

                for i in range(len(resultsValidatedUser)):
                    for j in range(len(characters)):
                        resultsValidatedUser[i] = str(resultsValidatedUser[i]).replace(characters[j], "")
                    resultsValidatedUser = str(resultsValidatedUser[i])

                cursor.close()



                DateStart = input("Enter Date Start with format: YYYY-MM-DD \n")
                DateStart = DateStart.upper()
                DateFinish = input("Enter Date Finish with format:YYYY-MM-DD \n")
                DateFinish = DateFinish.upper()
                CountryBooking = input("Enter Country booking \n")
                CountryBooking = CountryBooking.upper()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT PlaceID FROM Place")
                resultsPlaceId = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT Description FROM Place")
                resultsDescription = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT Country FROM Place")
                resultsCountry = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT Price FROM Place")
                resultsPrice = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT Address FROM Place")
                resultsAddress = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT NameContact FROM Place")
                resultsNameContact = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT PhoneContact FROM Place")
                resultsPhoneContact = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT AvailabilityStart FROM Place")
                resultsAvailabilityStart = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    "SELECT AvailabilityEnd FROM Place")
                resultsAvailabilityEnd = cursor.fetchall()
                cursor.close()

                characters = "(',)"



                for i in range(len(resultsPlaceId)):
                    for j in range(len(characters)):
                        resultsAvailabilityStart[i] = str(resultsAvailabilityStart[i]).replace(characters[j],"")
                        resultsAvailabilityEnd[i] = str(resultsAvailabilityEnd[i]).replace(characters[j],"")
                        resultsCountry[i] = str(resultsCountry[i]).replace(characters[j],"")
                    if(resultsCountry[i] == CountryBooking):
                        if((datetime.datetime.strptime(DateStart, '%Y-%m-%d'))<(datetime.datetime.strptime(DateFinish, '%Y-%m-%d'))):
                            if((datetime.datetime.strptime(DateStart, '%Y-%m-%d')>=datetime.datetime.strptime(str(resultsAvailabilityStart[i]), '%Y-%m-%d')) and (datetime.datetime.strptime(DateFinish, '%Y-%m-%d')>=datetime.datetime.strptime(str(resultsAvailabilityStart[i]), '%Y-%m-%d'))):
                                if((datetime.datetime.strptime(DateStart, '%Y-%m-%d')<=datetime.datetime.strptime(str(resultsAvailabilityEnd[i]), '%Y-%m-%d')) and (datetime.datetime.strptime(DateFinish, '%Y-%m-%d')<=datetime.datetime.strptime(str(resultsAvailabilityEnd[i]), '%Y-%m-%d'))):
                                    print("\nPlaces: Place ID:" + str(resultsPlaceId[i]) + "\n")
                                    print("Description:" + str(resultsDescription[i]) + "\n")
                                    print("Country:" + str(resultsCountry[i]) + "\n")
                                    print("Price:" + str(resultsPrice[i]) + "\n")
                                    print("Address:" + str(resultsAddress[i]) + "\n")
                                    print("NameContact:" + str(resultsNameContact[i]) + "\n")
                                    print("PhoneContact:" + str(resultsPhoneContact[i]) + "\n")
                                    print("AvailabilityStart:" + str(resultsAvailabilityStart[i]) + "\n")
                                    print("AvailabilityEnd:" + str(resultsAvailabilityEnd[i]) + "\n")
                                    exit = True
                    #else:
                     #   print("\n There is not availability for the country selected, please try again \n")



                if (exit):
                    selectedplaceID= input("Select ID place to booking: \n")
                    selectedplaceID = selectedplaceID.upper()

                    cursor = connection.cursor()
                    cursor.execute(
                        "INSERT INTO Booking (BookingDateStart, BookingFinishDate, UserID, PlaceID ) "
                        "values ('" + DateStart + "','" + DateFinish + "','" + resultsValidatedUser + "','" +
                        selectedplaceID + "');")
                    cursor.execute("COMMIT;")
                    cursor.close()
                    # --------------------------------------------------------------------------------
                    print("\nThe booking was successfully created\n")
                else:
                    print("\n There is not availability for the country selected, please try again \n")
            else:
                print("\n User Incorrect, please try again \n")


    elif option == 4:
            count = ''
            print("\n**********************************************")
            print("*******************REPORTS**********************")
            print("************************************************")
            email = input("Enter your email: \n")
            email = email.upper()
            password = input("Enter your password: \n")
            password = password.upper()

            connection = sqlite3.connect("Travel_Agency.db")
            # --------------------------------------------------------------------------------
            cursor = connection.cursor()
            cursor.execute(
                "SELECT UserName FROM User WHERE UserName = '" + email + "' and  UserType =  '0'")
            resultsValidatedAdmin = cursor.fetchone()
            cursor.close()
            manageReport = True
            if resultsValidatedAdmin != None:
                while(manageReport):

                    print("\n***************SELECT REPORT**************\n (1) BooKings  By Country \n", "(2) BooKings  By User\n", "(3) Average Price by booking Type\n")
                    optionReport = input("Select the Option:")
                    optionReport = int(optionReport)

                    if optionReport == 1:
                        print("\n**********************************************")
                        print("************1. BooKings  By Country*************")
                        print("************************************************")


                        conn = sqlite3.connect('Travel_Agency.db')
                        sql_query = pd.read_sql_query('''
                                                    
                                                        
                                                        SELECT c.Country, COUNT(b.UserID)
                                                        FROM 
                                                        Booking a, User b, Place c 
                                                        where a.UserID = b.UserID
                                                        and a.PlaceID = c.PlaceID 
                                                        GROUP BY c.Country
                                                       ''', conn)

                        fig, ax = plt.subplots()

                        # hide axes
                        fig.patch.set_visible(False)
                        ax.axis('off')
                        ax.axis('tight')

                        df = pd.DataFrame(sql_query, columns=['Country', 'COUNT(b.UserID)'])
                        ax.table(cellText=df.values, colLabels=df.columns, loc='center')

                        fig.tight_layout()
                        plt.show()
                        #print(df)
                        # define figure and axes

                        # create table
                        #table = plt.table(cellText=df.values, colLabels=df.columns, loc='center')

                        # display table

                        #plt.show()
                        connection.close()

                        #table_query= plt.table(cellText=df.values),
                        #rowLabels=df.index.tolist(),
                        #colLabels=df.columns.tolist(),
                        #cellLoc='left',
                        #rowLoc='left')

                        #plt.show()

                        #plt.plot([1, 2, 3, 4])
                        #plt.ylabel('y-axis')
                        #plt.xlabel('x-axis')
                        #plt.show()

                    if optionReport == 2:
                            count = ''
                            print("\n**********************************************")
                            print("***+++++++**2.  BooKings  By User***************")
                            print("************************************************")

                            conn = sqlite3.connect('Travel_Agency.db')
                            sql_query = pd.read_sql_query('''
        
                                                            select  b.UserName, COUNT(b.UserName) 
                                                            FROM
                                                            Booking a, User b, Place c 
                                                            where a.UserID = b.UserID
                                                            and a.PlaceID = c.PlaceID 
                                                            group by b.UserName
                                                            order by b.UserName
                                                           ''', conn)

                            fig, ax = plt.subplots()

                            # hide axes
                            fig.patch.set_visible(False)
                            ax.axis('off')
                            ax.axis('tight')

                            df = pd.DataFrame(sql_query, columns=['UserName', 'COUNT(b.UserName)'])
                            ax.table(cellText=df.values, colLabels=df.columns, loc='center')

                            fig.tight_layout()
                            plt.show()
                            # print(df)
                            # define figure and axes

                            # create table
                            # table = plt.table(cellText=df.values, colLabels=df.columns, loc='center')

                            # display table

                            # plt.show()
                            connection.close()

                    if optionReport == 3:
                            count = ''
                            print("\n**********************************************")
                            print("*****3. Average Price by booking Type***********")
                            print("************************************************")

                            conn = sqlite3.connect('Travel_Agency.db')
                            sql_query = pd.read_sql_query('''
        
                                                            
                                                            
                                                            SELECT     c.Description, round(AVG(c.Price))
                                                            FROM       
                                                            Booking a, User b, Place c 
                                                            where a.UserID = b.UserID
                                                            and a.PlaceID = c.PlaceID 
                                                            GROUP BY   c.Description;
                                                           ''', conn)

                            fig, ax = plt.subplots()

                            # hide axes
                            fig.patch.set_visible(False)
                            ax.axis('off')
                            ax.axis('tight')

                            df = pd.DataFrame(sql_query, columns=['Description', 'round(AVG(c.Price))'])
                            ax.table(cellText=df.values, colLabels=df.columns, loc='center')

                            fig.tight_layout()
                            plt.show()
                            # print(df)
                            # define figure and axes

                            # create table
                            # table = plt.table(cellText=df.values, colLabels=df.columns, loc='center')

                            # display table

                            # plt.show()
                            connection.close()



                    elif optionReport == 4:
                        manageReport = False
            else:
                print("\n The user or password is not correct try again, please \n")

    elif option == 5:
        start = False


