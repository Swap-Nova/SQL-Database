import sqlite3
conn_882=sqlite3.connect('week4.db')

print("Opened database successfully")
conn_882.execute("CREATE TABLE recipes(id INT PRIMARY KEY NOT NULL,name VARCHAR,description TEXT,category_id INT,chef_id text,created DATETIME)");

print("Table created successfully")

conn_882.execute("INSERT INTO recipes VALUES(101,'Chicken Curry','Indian',01,'BL00001','2022-02-14');")
conn_882.execute("INSERT INTO recipes VALUES(102,'Ramen','Japanese',02,'BL00002','2022-02-14');")
conn_882.execute("INSERT INTO recipes VALUES(103,'Tacos','Mexican',03,'BL00003','2022-02-14');")
conn_882.execute("INSERT INTO recipes VALUES(104,'Pasta','Italian',04,'BL00004','2022-02-14');")

conn_882.commit()

print("Records inserted successfully");
print("\nDisplaying the table \n");

for rows in conn_882.execute("SELECT * from recipes;"):
    print(rows)
    print("\nPART A\n")
for rows in conn_882.execute("SELECT * from recipes WHERE description='Japanese';"):
    print(rows)
    print("\nPART B\n")
for rows in conn_882.execute("SELECT id,name from recipes WHERE chef_id='BL00002';"):
    print(rows)
    print("\nPART C\n")
for rows in conn_882.execute("SELECT description from recipes WHERE name LIKE 'P%';"):
    print(rows)
conn_882.close()