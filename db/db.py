# import mysql.connector as db

# connection=db.connect(host='localhost',username='root',password='7229420000',database="seemab")

# my_cursor=connection.cursor()

# my_cursor.execute("SHOW DATABASES")
# my_cursor.execute("CREATE DATABASES seemab")
# my_cursor.execute("SHOW DATABASES")
# my_cursor.execute("CREATE TABLE student(name VARCHAR(255),age INT)")
# values=[
#     ("Hamza",24),
#     ("Hamza",22),
#     ("Hamza",26),
#     ("Hamza",2),
#     ("Hamza",4),
#     ("Hamza",254),
#     ("Hamza",254),
#     ("Hamza",264),
#     ("Hamza",254)
# ]
# my_cursor.executemany("INSERT INTO student(name,age) VALUES(%s,%s)",values)

# my_cursor.execute("SELECT * FROM student")




# for i in my_cursor:
#     print(i)

# print(my_cursor.fetchall())

# connection.commit()
# connection.close()