from config.db import connect_db
from typing import Dict, Any, List
from datetime import date

@connect_db
def insert_counselor(conn, cid:int, fname:str, lname:str, age:int, position:str, prof_started:date):
    try:
        cur = conn.cursor()
        sql = 'insert into counselor (id, cid, firstname, lastname, age, position, profession_started) values (%s, %s, %s, %s, %s, %s,%s)'
        values = (id, cid, fname, lname, age, position, prof_started)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False