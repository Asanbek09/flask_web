from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_patient(conn, id:int, fname:str, lname:str, age:int, gender:str, civil_status:str, address:str, mobile:str, occupation:str, nationality:str, cid:str, counsel_started:date, counsel_ended:date):
    try:
        cur = conn.cursor()
        sql = 'insert into patient(id, firstname, lastname, age, gender, civil_status, address, mobile, occupation, nationality, cid, counseling_started, counseling_ended)'
        values = (id, fname, lname, age, gender, civil_status, address, mobile, occupation, nationality, cid, counsel_started, counsel_ended)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

