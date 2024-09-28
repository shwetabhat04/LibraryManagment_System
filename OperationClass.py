import sqlite3



class LibManager:

    def __init__(self):
        self.conn = sqlite3.connect("MyLibrary.db")
        self.cursor = self.conn.cursor()


    def Add_book(self,name, author,count):
        # Insert into table 
        self.cursor.execute('''
                        INSERT INTO Books (name, author,count) VALUES (?,?,?)
                        ''', (name, author,count)
                    )
        self.conn.commit()

    def Display_books(self):

        self.cursor.execute(''' 
                        SELECT * FROM Books
                    ''')
        
        all_books = self.cursor.fetchall()

        if all_books:
            print("\n\nList of Books")
            print("bcode   | name   | author   | count")
            print("-------------------------------------")

            for book in all_books:
                print(f"{book[0]}  | {book[1]}   | {book[2]}  | {book[3]}")
        
        else:
            print("No books are available")

        self.conn.commit()

    def return_book(self,rolno,bookcode):
        # Insert into table 
        self.cursor.execute('''
                        DELETE FROM Issued WHERE rollno = ? AND bookcode = ?
                        ''', (rolno,bookcode)
                    )
        self.conn.commit()

    def issue_book(self,student_name,rolno,bookcode):
        # Insert into table 
        self.cursor.execute('''
                        INSERT INTO Issued (student_name, rollno,bookcode) VALUES (?,?,?)
                        ''', (student_name, rolno,bookcode)
                    )
        self.conn.commit()

    def Display_issued(self):
        self.cursor.execute(''' 
                        SELECT * FROM Issued
                    ''')
        
        all_rows = self.cursor.fetchall()

        if all_rows:
            print("\n\nList of Issued Names")
            print("Student Name  | Rollno   | bookcode ")
            print("-------------------------------------")

            for row in all_rows:
                print(f"{row[0]}  | {row[1]}   | {row[2]} ")
        
        else:
            print("No user are available")

        self.conn.commit()


if __name__ == "__main__":

    LibObject = LibManager()

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
        LibObject.Add_book(name,author,int(count))
        LibObject.Display_books()

    elif selection == 2:
        #issue_book(student_name,rolno,bookcode)
        print("Available Books")
        LibObject.Display_books()
        student_name = input("\n Enter Student Name: ")
        rollno = input(" Enter Roll No.: ")
        bookid = input(" Enter Book ID : ")
        LibObject.issue_book(student_name,int(rollno),int(bookid))
        LibObject.Display_issued()

    elif selection == 3:
        LibObject.Display_issued()
        rollno = input(" Enter Roll No.: ")
        bookid = input(" Enter Book ID : ")
        LibObject.return_book(int(rollno),int(bookid))
        LibObject.Display_issued()
