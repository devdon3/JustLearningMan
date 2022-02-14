from datetime import datetime
from datetime import timedelta
from datetime import date
import mysql.connector
# Making connection with MySQL
try:
    con = mysql.connector.connect(
        host = "localhost",
        user="root",
        passwd="",
        database="")
except Exception as e:
    if "Access denied" in str(e):
        print("\n!!!PLEASE ENTER VALID PASSWORD!!!!\n")
    if "Unknown database" in str(e):
        print("\n!!!PLEASE ENTER VALID DATABASE!!!\n")
try:
    cursor = con.cursor()
    # checking if table already exists
    cursor.execute("SHOW TABLES")
    s = cursor.fetchall()
    #If there is atleast one table in database
    if s!=[]:
        print("\nUsing old table....\n")
        # If table named "library_system" doesnt't exist
        if "library_system" not  in (s[0]):
            cursor.execute("""CREATE TABLE library_system(
                Book_ID INT PRIMARY KEY,
                Name CHAR(200),
                Author CHAR(200),
                Issued CHAR(3),
                Name_of_issuer CHAR(200),
                Issued_date CHAR(10),
                Return_date CHAR(10)        
            )""")
        # If table named "library_system" exist
        else:
            pass
    # If there is no table in database we will directly create the database
    else:
        print("\nCreating new table.....\n")
        cursor.execute("""CREATE TABLE library_system(
                Book_ID INT PRIMARY KEY,
                Name CHAR(200),
                Author CHAR(200),
                Issued CHAR(3),
                Name_of_issuer CHAR(200),
                Issued_date CHAR(10),
                Return_date CHAR(10) 
                
            )""")
except Exception as e:
    exit()
#while statement will help in using the program multiple times
while True:
    #using try statement to handle exceptions in main menu
    try:
        print('''
        [0]\t Exit
        [1]\t Display all the books
        [2]\t Insert new book record
        [3]\t Update book record
        [4]\t Delete book record
        [5]\t Search book
        [6]\t Display issued books
        [7]\t Display non-issued books
        [8]\t Issue a book
        [9]\t Return a book
        ''')
        choice = int(input("Enter your choice:\t"))
        # Choices is given between 0 and 9 so any other number will be neglected
        if choice >=0 and choice<=9:
            # Exit choice
            if choice  == 0:
                print("\nBye!!!!\n")
                break
            if choice == 1:
                #Reading whole table
                cursor.execute("SELECT * FROM library_system")
                read = cursor.fetchall()
                maxi = 0
                # finding out the longest word in whole table
                for i in read:
                    for j in i:
                        if len(str(j))>maxi:
                            maxi = len(str(j))
                size = max( len("| Name_of_issuer"),(maxi+2))
                print()
                # Making a table in python like MySQL
                size1 = size+1
                size2 = size-2
                msize = size-1
                print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                # Printing data from list read
                for (i) in read:
                    # printing data from tuple i
                    print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                # Ending the table
                print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
            # Option to insert new book                 
            if choice == 2:
                for i in range(int(input("How many books do you want to add?:\t"))):
                    print()
                    book_id = input("Enter book id:\t")
                    name = input("Enter book name:\t")
                    author = input("Enter name of author:\t")
                    command="INSERT INTO library_system(Book_ID,Name,Author,Issued) VALUES(%s,%s,%s,%s)"# %s specifies different values for the variable with index in tuple data
                    data  = (book_id,name,author,"No")#created a tuple for variables used in command variable
                    try:
                        cursor.execute(command,data)
                    except Exception as e:
                        print(e)
                
            # Option to update book record
            if choice == 3:
                while True:
                    try:
                        #Reading whole table
                        cursor.execute("SELECT * FROM library_system")
                        read = cursor.fetchall()
                        maxi = 0
                        # finding out the longest word in whole table
                        for i in read:
                            for j in i:
                                if len(str(j))>maxi:
                                    maxi = len(str(j))
                        size = max( len("| Name_of_issuer"),(maxi+2))
                        print()
                        # Making a table in python like MySQL
                        size1 = size+1
                        size2 = size-2
                        msize = size-1
                        print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                        print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                        print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                        # Printing data from list read
                        for (i) in read:
                            # printing data from tuple i
                            print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                        # Ending the table
                        print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                        print('''
                            [0] Main Menu
                            [1] Book Name
                            [2] Author Name
                        ''')
                        update_choice = int(input("Enter your choice for data update:\t"))
                        # On input of value greater than 3 or less than 0 the program for update will run again
                        if update_choice >=0 and update_choice <=2:
                            if update_choice == 0:
                                break
                            if update_choice == 1:
                                book_id = int(input("Enter book_id you want to update:\t"))
                                new_book_name = (input("Enter new Book name:\t"))
                                command = "UPDATE library_system SET Name=%s WHERE Book_id=%s"
                                data = (new_book_name,book_id)
                                cursor.execute(command,data)
                            if update_choice==2:
                                book_id = int(input("Enter book_id you want to update:\t"))
                                new_author_name = input("Enter new author name:\t")
                                command = "UPDATE library_system SET Author=%s WHERE Book_id=%s"
                                data = (new_author_name,book_id)
                                cursor.execute(command,data)
                            con.commit()
                        else:
                            print("\nPlease enter value between 0 and 2 !!!!\n")
                    except Exception as e:
                        print(e)
               
            # Option to delete a book record
            if choice == 4:
                while True:
                    try:
                        #Reading whole table
                        cursor.execute("SELECT * FROM library_system")
                        read = cursor.fetchall()
                        maxi = 0
                        # finding out the longest word in whole table
                        for i in read:
                            for j in i:
                                if len(str(j))>maxi:
                                    maxi = len(str(j))
                        size = max( len("| Name_of_issuer"),(maxi+2))
                        print()
                        # Making a table in python like MySQL
                        size1 = size+1
                        size2 = size-2
                        msize = size-1
                        print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                        print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                        print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                        # Printing data from list read
                        for (i) in read:
                            # printing data from tuple i
                            print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                        # Ending the table
                        print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                        # Just add multiple id's or single id and it will split the id and convert it into list
                        book_id = list(map(int,input("Please Enter all the book ids you want to delete (with space):\t").split()))
                        for i in book_id:
                            cursor.execute("DELETE FROM library_system WHERE Book_id=%s",(str(i),))
                            
                        break
                    except Exception as e:
                        print(e)
            # Option for searching in the record
            if choice == 5:
                while True:
                    print()
                    try:
                        print('''
                        [0] Exit
                        [1] Search with Book ID
                        [2] Search with Book Name
                        [3] Search with Author Name
                        ''')    
                        search_choice = int(input("Enter how do you want ot search in the database:\t"))
                        if search_choice>=0 and search_choice<=3:
                            if search_choice == 0:
                                break
                            if search_choice == 1:
                                while True:
                                    try:
                                        # Taking input for book ID
                                        book_id = int(input("Enter book id:\t"))
                                        # search in the table row with book ID
                                        cursor.execute("SELECT * FROM library_system WHERE Book_ID=%s",(book_id,))
                                        read = cursor.fetchall()
                                        if read !=[]:
                                            maxi = 0
                                            # finding out the longest word in whole table
                                            for i in read:
                                                for j in i:
                                                    if len(str(j))>maxi:
                                                        maxi = len(str(j))
                                            size = max( len("| Name_of_issuer"),(maxi+2))
                                            print()
                                            # Making a table in python like MySQL
                                            size1 = size+1
                                            size2 = size-2
                                            msize = size-1
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                                            print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                                            # Printing data from list read
                                            for (i) in read:
                                                # printing data from tuple i
                                                print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                                            # Ending the table
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                                            break
                                        else:
                                            print("\n!!!!!!!!No record found. Please enter a valid book ID.!!!!!!\n")
                                    except Exception as e:
                                        print(e)   
                            if search_choice == 2:
                                while True:
                                    try:
                                        # Taking input for book name
                                        book_name = (input("Enter book name(Enter 0 to search with another way):\t"))
                                        if book_name=="0":
                                            break
                                        # search in the table row with book name
                                        cursor.execute("SELECT * FROM library_system WHERE Name=%s",(book_name,))
                                        read = cursor.fetchall()
                                        if read !=[]:
                                            maxi = 0
                                            # finding out the longest word in whole table
                                            for i in read:
                                                for j in i:
                                                    if len(str(j))>maxi:
                                                        maxi = len(str(j))
                                            size = max( len("| Name_of_issuer"),(maxi+2))
                                            print()
                                            # Making a table in python like MySQL
                                            size1 = size+1
                                            size2 = size-2
                                            msize = size-1
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                                            print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                                            # Printing data from list read
                                            for (i) in read:
                                                # printing data from tuple i
                                                print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                                            # Ending the table
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                                            break
                                        else:
                                            print("\n!!!!!!!!No record found. Please enter a valid book Name.!!!!!!\n")
                                    except Exception as e:
                                        print(e)    
                            if search_choice == 3:
                                while True:
                                    try:
                                        # Taking input for author name
                                        author = (input("Enter author name(Enter 0 to search with another way):\t"))
                                        if author=="0":
                                            break
                                        # search in the table row with author name
                                        cursor.execute("SELECT * FROM library_system WHERE Author=%s",(author,))
                                        read = cursor.fetchall()
                                        if read !=[]:
                                            maxi = 0
                                            # finding out the longest word in whole table
                                            for i in read:
                                                for j in i:
                                                    if len(str(j))>maxi:
                                                        maxi = len(str(j))
                                            size = max( len("| Name_of_issuer"),(maxi+2))
                                            print()
                                            # Making a table in python like MySQL
                                            size1 = size+1
                                            size2 = size-2
                                            msize = size-1
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                                            print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                                            # Printing data from list read
                                            for (i) in read:
                                                # printing data from tuple i
                                                print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                                            # Ending the table
                                            print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                                            break
                                        else:
                                            print("\n!!!!!!!!No record found. Please enter a valid Author Name.!!!!!!\n")
                                    except Exception as e:
                                        print(e)                                        
                        else:
                            print("\nPlease enter a valid number between 0 and 3!!!!!!!!!\n")
                        
                    except Exception as e:
                        print(e)    
            # Option to display all issued books
            if choice == 6:
                cursor.execute("SELECT * FROM library_system WHERE Issued='Yes'")
                read = cursor.fetchall()        
                if read !=[]:
                    maxi = 0
                    # finding out the longest word in whole table
                    for i in read:
                        for j in i:
                            if len(str(j))>maxi:
                                maxi = len(str(j))
                    size = max( len("| Name_of_issuer"),(maxi+2))
                    print()
                    # Making a table in python like MySQL
                    size1 = size+1
                    size2 = size-2
                    msize = size-1
                    print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                    print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                    print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                    # Printing data from list read
                    for (i) in read:
                        # printing data from tuple i
                        print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                    # Ending the table
                    print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                    
                else:
                    print("\n!!!!!!!!There is no book issued!!!!!!\n")            
            # Option to display all issuable/non-issued books              
            if choice == 7:
                cursor.execute("SELECT * FROM library_system WHERE Issued='No'")
                read = cursor.fetchall()        
                if read !=[]:
                    maxi = 0
                    # finding out the longest word in whole table
                    for i in read:
                        for j in i:
                            if len(str(j))>maxi:
                                maxi = len(str(j))
                    size = max( len("| Name_of_issuer"),(maxi+2))
                    print()
                    # Making a table in python like MySQL
                    size1 = size+1
                    size2 = size-2
                    msize = size-1
                    print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                    print("| Book_ID"+" "*(size -len("| Book_ID"))+"| Name"+" "*(size1-len("| Name"))+"| Author"+" "*(size1-len("| Author"))+"| Issued"+" "*(size1-len("| Issued"))+"| Name of Issuer"+" "*(size1-len("| Name of issuer"))+"| Issued Date"+" "*(size1-len("| Issued Date"))+"| Return date"+" "*(size1-len("| Return date"))+"|")
                    print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")     
                    # Printing data from list read
                    for (i) in read:
                        # printing data from tuple i
                        print("| "+str(i[0])+" "*((size2)-len(str(i[0])))+"| "+str(i[1])+" "*(msize-len(str(i[1])))+"| "+str(i[2])+" "*(msize-len(str(i[2])))+"| "+str(i[3])+" "*(msize-len(str(i[3])))+"| "+str(i[4])+" "*(msize-len(str(i[4])))+"| "+str(i[5])+" "*(msize-len(str(i[5])))+"| "+str(i[6])+" "*(msize-len(str(i[6])))+"|")              
                    # Ending the table
                    print( "+"+"-"*(size-1)+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+"+"-"*size+"+")
                    
                else:
                    print("\n!!!!!!!!There is no book issued!!!!!!\n")     
            # Option to issue a book
            if choice == 8:
                while True:
                    book_id = int(input("Enter book ID to issue a book:\t"))   
                    # Checking if book with 'book_id' exists and if it is issued or not
                    cursor.execute("SELECT * FROM library_system WHERE Book_ID=%s and Issued='No'",(book_id,))
                    read = cursor.fetchall()
                    # If book exists and it is not issued
                    if read!=[]:
                        name_of_issuer = input("Student name:\t")
                        Begindate = date.today()# Adding today's date in issued date
                        Enddate = Begindate + timedelta(days=14) # Return date is after 2 week ,i.e., 14 days
                        # Converted time to strings
                        Begindate = Begindate.strftime("%d-%m-%Y")
                        Enddate = Enddate.strftime("%d-%m-%Y")
                        cursor.execute("UPDATE library_system SET Issued='Yes', Name_of_issuer=%s, Issued_date=%s, Return_date=%s WHERE Book_ID=%s",(name_of_issuer,Begindate,Enddate,book_id))
                        break
                    # if book is issued
                    else:
                        print("!!Book is alread issued !!")                    
            # Option to return a book
            if choice == 9:
                book_id = int(input("Enter book ID:\t"))
                # Checking if book with 'book_id' exists and if it is issued or not
                cursor.execute("SELECT * FROM library_system WHERE Book_ID=%s and Issued='Yes'",(book_id,))
                # Reading data of the table
                read = cursor.fetchall()
                
                if read!=[]:
                    # fetched return date from the table and converted it into datetime format
                    return_date = datetime.strptime(str(read[0][6]),"%d-%m-%Y")
                    # If there the student is returning book in given time
                    if return_date>=datetime.today():
                        print("Returning Book!!")
                    #If the student does not return book in time fine of Rs. 1 will be taken each day 
                    else:
                        print("Please take fine of Rs.", datetime.today()-return_date)
                    cursor.execute("UPDATE library_system SET Issued='No', Name_of_issuer=NULL, Issued_date=NULL, Return_date=NULL WHERE Book_ID=%s",(book_id,))
                #If the book is not issued or doesn't exist in the data
                else:
                    print("The book is not issued")
        #This statement will work when main menu choice doesn't fall in  range for the program       
        else:
            print("Please choose a choice between 0 and 9!!!!")
        con.commit()# Final commit to the database
    except Exception as e:
        print(e)