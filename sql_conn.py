from tkinter import E, EXCEPTION

from numpy import roll
import cx_Oracle

def add_entry(roll_no, name, marks):
    try:
        roll_no, marks = int(roll_no), int(marks)
    except EXCEPTION as e:
        print(e)

    sql_query = 'INSERT INTO sql_conn VALUES (:r, :n, :m)'
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name = 'XE')
        conn = cx_Oracle.connect(user = r'shriniket', password = 'shriniket', dsn = dsn_tns)              #bug user
        c = conn.cursor()
        c.execute(sql_query, [int(roll_no), name, int(marks)])
        conn.commit()
    except cx_Oracle.Error as e:
        print(e)

    c.execute('SELECT * FROM sql_conn')
    for rows in c:
        print(rows[0], '-', rows[1], '-', rows[2], '\n')
        conn.commit()
        c.close()

def delete_entry(sql, del_query):
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name = 'XE')
        conn = cx_Oracle.connect(user = r'shriniket', paasword = 'shriniket', dsn = dsn_tns)
        c = conn.cursor()
        c.execute(sql,[del_query])
        conn.commit()

    except Exception as e:
        print(e)
    c.execute('SELECT * FROM sql_conn')
    for data in c:
        print(data[0], '-', data[1], '-', data[2], '\n')
        c.close()

def update_entry(roll_no, name, marks):
    print('here')
    try:
        roll_no, marks = int(roll_no), int(marks)
    except EXCEPTION as e:
            error_1 = e
            return error_1
        
    sql_query = 'UPDATE sql_conn SET name = :n, marks = :m WHERE roll_no = :r'
    try:
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name = 'XE')
        conn = cx_Oracle.connect(user = r'shriniket', paasword = 'shriniket', dsn = dsn_tns)
        c = conn.cursor()
        print('trying')
        c.execute(sql_query,[name, marks, roll_no])
        print('trying')
    except cx_Oracle.Error as e:
        print(e)
        error_1 = e
        return error_1

    c.execute('SELECT * FROM sql_conn')
    for rows in c:
        print(rows[0], '-', rows[1], '-', rows[2], '\n')
        conn.commit()
        c.close()

while True:
    inp = input("1. ADD\n2.DELETE\n4.Show entry \n ENTER INPUT:")
    print(' ')
    match inp:
        case '1':
            roll_no, name, marks = map(str, input("enter roll no name and marks seperated by space:").split())
            add_entry(roll_no, name, marks)
        case '2':
            sql = 'DELETE FROM sql_conn WHERE roll_no = :r'
            del_query = int(input("Enter roll no to delete:"))
            delete_entry(sql, del_query)
        case '3':
            roll_no, name, marks = map(str, input("enter roll no name and marks seperated by space:").split())
            update_entry(roll_no, name, marks)
        case '4':
            dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name = 'XE')
            conn = cx_Oracle.connect(user = r'shriniket', paasword = 'shriniket', dsn = dsn_tns)
            c = conn.cursor()
            c.execute('select * from sql_conn')
            for r in c:
                print(r[0], '-', r[1], '-', r[2], '\n')

