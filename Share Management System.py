#Created by Harshit Vijay Kumar and Puru Jindal
import mysql.connector
def Share():
    print("-----------------------SHARE MANAGEMENT SYSTEM--------------------")
    print("Hey there welcome, sorry for bothering your experience but ")
    user_n = input("Please tell us the username of your system ",)
    passw = input("Please tell us the password of your system ",)
    zuko = 1                                                                                      # Looping
    while zuko == 1:
        try:
            global mydb
            mydb = mysql.connector.connect(host = "localhost", user = user_n, password = passw)
            # This is used to input custom username and password
            global mycursor
            #This enables the program to be able to run on any system
            mycursor = mydb.cursor()
            zuko = 0
            print("Sorry to interrupt but have you been here before? ")
            print("1.Yes, I know the ropes")
            #You already have the database created
            print("2.No, newbie")
            #No I wounld need the database to be created
            o = 0
            while o == 0:
                try:
                    ab = int(input("So, is this a memory or deja vu ",))
                    if ab in [1,2]:
                        o = 1
                        if ab == 2:
                            databse()
                        if ab == 1:
                            check()
                    else:
                        print("There was no third option")
                except:
                    print("Please enter an integer value")

        
            p = 1
            print("-------------------------MENU--------------------------------")
            print("1. Add a company")
            print("2. Add a share")
            print("3. See all the available companies")
            print("4. See all the available shares")
            print("5. Delete all the data")
            print("6. Delete a Company")
            print("7. Delete a Share")
            print("8. Exit")
            while p == 1:
                try:
                    a = int(input("What do you want to do today "))
                    if a in [1,2,3,4,5,6,7,8]:
                        if a == 1:
                            company()
                        if a == 2:
                            share()
                        if a == 3:
                            company_print()
                        if a == 4:
                            share_print()
                        if a == 5:
                            b = str(input("Are you sure, any data you added would be lost "))
                            if b.lower() in ["yes","y"]:
                                drop_database()
                                p = 2
                            if b.lower() in ["no","n"]:
                                print("Understandable, Have a Great Day")
                            if b.lower() not in ["yes","y","no","n"]:
                                print("Please answer in yes or no only")
                        if a == 6:
                            try:
                                c = str(input("Are you sure, data you added would be lost "))
                                if c.lower() in ["yes","y"]:
                                    drop_table()
                                if c.lower() in ["no","n"]:
                                    print("Understandable, Have a Great Day")
                                if c.lower() not in ["yes","y","no","n"]:
                                    print("Please answer in yes or no only")
                            except:
                                print("We have no knowledge of such a company")
                        if a == 7:
                            d = str(input("Are you sure "))
                            if d.lower() in ["yes","y"]:
                                drop_record()
                            if d.lower() in ["no","n"]:
                                print("Understandable, Have a Great Day")
                            if d.lower() not in ["yes","y","no","n"]:
                                print("Please answer in yes or no only")
                        if a == 8:
                            p = 2

                    else:
                        print("Sorry you expected more options but if it is any consolation this is not the final product")
                except:
                    print("Please enter an integer value")
        except:
            print("The username or password is wrong")
            break





def check():
    try:
        mycursor.execute("USE ShareManagementSystem")
        #Checks if you have the database
    except:
        print("You lied to me, this is why I have trust issues")
        #If you do not have it , it is created
        databse()
def databse():
    try:
        mycursor.execute("CREATE DATABASE ShareManagementSystem")
        #Creates databse
        check()
    except:
        print("I know you ....... user")
        #If exception occurs than this line of code is executed
def company():
    comp = str(input("What is the name of the company "))
    try:
        sql = "CREATE TABLE " + (comp) + " (Name VARCHAR(200) ,Current_Rate INT(5) ,Week_Highest INT(10) ,Week_Lowest INT(10))"           #Adds a company
        mycursor.execute(str(sql))
        print("Your company was added")
    except:
         print("A company with such a name already exists")
def share():
    g = input("What company share are you looking for? ")
    #Make a loop which confirms that this company exists
    name = str(input("Enter the name of the share "))
    cur_rate = int(input("Enter the current rate of the share "))
    week_high = int(input("What was the week highest for that share "))
    week_low = int(input("What was the week lowest for the share "))
    s = "INSERT INTO " + (g) + " (Name,Current_Rate,Week_highest,Week_Lowest) VALUES (%s,%s,%s,%s)"
    v = (name,cur_rate,week_high,week_low)
    mycursor.execute(s,v)
    mydb.commit()
    print("Your share was added")
def share_print():
    g = str(input("What company shares are you looking for? "))
    L =[]
    try:
        sql = "SELECT * FROM " + (g)
        mycursor.execute(str(sql))
        result = mycursor.fetchall()
        for x in result:
            L.append(x)
            print(x)
        if L == []:
            print("There are no shares in this company yet")
    except:
        print("No company with such a name exists")
def company_print():
    mycursor.execute("SHOW TABLES")
    L = []
    result = mycursor.fetchall()
    for x in result:
        L.append(x)
        print(x)
    if L == []:
        print("There are no companies available yet")
def drop_database():
    mycursor.execute("DROP DATABASE ShareManagementSystem")
    print("Your work was done")
def drop_table():
    g = str(input("Please enter the name of the company "))
    try:
        mycursor.execute("DROP TABLE " + (g))
        print("Your work was done")
    except:
        print("No company with this name exists")
def drop_record():
    g = input("What company share are you looking for? ")  
    name = str(input("Enter the name of the share "))
    try:
        mycursor.execute("DELETE FROM " + (g) + " WHERE Name = '" + (name) + "'" )
        mydb.commit()
        print("Your work was done")
    except:
         print("The company name or the share name is wrong")

Share()
