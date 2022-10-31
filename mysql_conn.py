# importing module
import cx_Oracle
#connection
con = cx_Oracle.connect('system/Akshay@//localhost:1521/xe')
# Now execute the sqlquery
cur = con.cursor() #a temporary work area created in system
#memory when a SQL statement is executed

# Creating a table employee
cur.execute("create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
print("Table Created successfully")

# Inserting a record into table employee
cur.execute('insert into employee values(10001,\'Rahul\',50000.50)')
# commit() to make changes reflect in the database
con.commit()
print('Record inserted successfully')

data = [[10007, 'Vikram', 48000.0], [10008, 'Sunil', 65000.1], [10009,
'Sameer', 75000.0]]
# Inserting multiple records into employee table
# (:1,:2,:3) are place holders. They pick data from a list supplied as
argument
cur.executemany('insert into employee values(:1,:2,:3)', data)

# To commit the transaction manually
con.commit()
print('Multiple records are inserted successfully')

#VIEW RESULTS
# fetchall() is used to fetch all records from result set
cur.execute('select * from employee')
rows = cur.fetchall()
print(rows)

# fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
cur.execute('select * from employee')
rows = cur.fetchmany(3)
print(rows)


# fetchone() is used fetch one record from top of the result set
cur.execute('select * from employee')
rows = cur.fetchone()
print(rows)
 
