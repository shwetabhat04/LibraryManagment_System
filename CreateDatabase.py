import sqlite3


# Connect to Database if exists else create one
conn = sqlite3.connect("MyLibrary.db")
cursor = conn.cursor()

# Create Books Database
cursor.execute('''
              CREATE TABLE IF NOT EXISTS Books (
               bcode INTEGER PRIMARY KEY,
               name TEXT TEXT NOT NULL,
               author TEXT TEXT NOT NULL,
               count INTEGER
                )
            '''
            )

# ISSUED TABLE CREATION 
cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS Issued(
                 student_name TEXT NOT NULL,
                 rollno INTEGER NOT NULL,
                 bookcode INTEGER NOT NULL,
                 
                 FOREIGN KEY (bookcode) REFERENCES Books(bcode)
                  
                )
            
                ''')


conn.commit()
conn.close()



