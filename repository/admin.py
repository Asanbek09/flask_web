from config.db import connect_db
from typing import Dict, Any, List
from datetime import date

@connect_db
def insert_admin(conn, id:int, fname:str, lname:str, age:int, position:str, emp_started:date, emp_status:bool):
    try:
        cur = conn.cursor()
        sql = 'insert into admin (id, firstname, lastname, age, position, emp_started, emp_status) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        values = (id, fname, lname, age, position, emp_started, emp_status)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False