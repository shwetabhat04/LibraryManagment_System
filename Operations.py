import sqlite3




def Add_book(name, author,count):
    conn = sqlite3.connect("MyLibrary.db")
    cursor = conn.cursor()

    # Insert into table 
    cursor.execute('''
                    INSERT INTO Books (name, author,count) VALUES (?,?,?)
                    ''', (name, author,count)
                   )
    conn.commit()
    conn.close()


def Display_books():
    conn = sqlite3.connect("MyLibrary.db")
    cursor = conn.cursor()

    cursor.execute(''' 
                    SELECT * FROM Books
                   ''')
    
    all_books = cursor.fetchall()

    if all_books:
        print("\n\nList of Books")
        print("bcode   | name   | author   | count")
        print("-------------------------------------")

        for book in all_books:
            print(f"{book[0]}  | {book[1]}   | {book[2]}  | {book[3]}")
    
    else:
        print("No books are available")

    conn.commit()
    conn.close()



def return_book(rolno,bookcode):
    conn = sqlite3.connect("MyLibrary.db")
    cursor = conn.cursor()

    # Insert into table 
    cursor.execute('''
                    DELETE FROM Issued WHERE rollno = ? AND bookcode = ?
                    ''', (rolno,bookcode)
                   )
    conn.commit()
    conn.close()




def issue_book(student_name,rolno,bookcode):
    conn = sqlite3.connect("MyLibrary.db")
    cursor = conn.cursor()

    # Insert into table 
    cursor.execute('''
                    INSERT INTO Issued (student_name, rollno,bookcode) VALUES (?,?,?)
                    ''', (student_name, rolno,bookcode)
                   )
    conn.commit()
    conn.close()


def Display_issued():
    conn = sqlite3.connect("MyLibrary.db")
    cursor = conn.cursor()

    cursor.execute(''' 
                    SELECT * FROM Issued
                   ''')
    
    all_rows = cursor.fetchall()

    if all_rows:
        print("\n\nList of Issued Names")
        print("Student Name  | Rollno   | bookcode ")
        print("-------------------------------------")

        for row in all_rows:
            print(f"{row[0]}  | {row[1]}   | {row[2]} ")
    
    else:
        print("No user are available")

    conn.commit()
    conn.close()





print("Enter Option")
print("1. Add Book")
print("2. Recieve Book")
print("3. Return Book")

selection = input("\n : ")
selection = int(selection)

if selection == 1:
    name = input("\n Enter Book Name: ")
    author = input(" Enter Author Name: ")
    count =  input(" Enter Book Count : ")
    Add_book(name,author,int(count))
    Display_books()

elif selection == 2:
    #issue_book(student_name,rolno,bookcode)
    print("Available Books")
    Display_books()
    student_name = input("\n Enter Student Name: ")
    rollno = input(" Enter Roll No.: ")
    bookid = input(" Enter Book ID : ")
    issue_book(student_name,int(rollno),int(bookid))
    Display_issued()

elif selection == 3:
    Display_issued()
    rollno = input(" Enter Roll No.: ")
    bookid = input(" Enter Book ID : ")
    return_book(int(rollno),int(bookid))
    Display_issued()
