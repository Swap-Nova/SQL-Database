import sqlite3
conn_882=sqlite3.connect('week4.db')
print("Opened database successfully")
conn_882.execute("CREATE TABLE movie(Movie_ID INT PRIMARY KEY NOT NULL,Movie_Name 
VARCHAR,Genre TEXT,Language text,Rating FLOAT);")
print("Table created successfully")
conn_882.execute("INSERT INTO movie VALUES(101,'Interstellar','Sci-fi','English',8.3);")
conn_882.commit()
conn_882.execute("INSERT INTO movie VALUES(102,'The Batman','Superhero','English',8.2);")
conn_882.commit()
conn_882.execute("INSERT INTO movie VALUES(103,'Top Gun','Action','English',8.0);")
conn_882.commit()
print("Records inserted successfully"); 
print("\nDisplaying the table \n")
for rows in conn_882.execute("SELECT * from movie;"):
 print(rows)
print("\nPART A\n")
conn_882.execute("UPDATE movie SET rating=rating+0.1*rating;")
print("Rating updated successfully")
for rows in conn_882.execute("SELECT * from movie;"):
 print(rows)
print("\nPART B\n")
conn_882.execute("DELETE from movie WHERE Movie_Id=102;")
print("\nRecord Deleted Successfully")
print("\nPART C\n")
for rows in conn_882.execute("SELECT * from movie WHERE rating>3;"):
 print(rows)
conn_882.close()
