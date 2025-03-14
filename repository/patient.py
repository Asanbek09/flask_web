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

@connect_db
def update_patient(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor()
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'update patient set {} where id = {}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_patient(conn, id:int):
    try:
        cur = conn.cursor()
        sql = 'delete from patient where id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_patient(conn):
    try:
        cur = conn.cursor()
        sql = 'select * from patient'
        cur.execute(sql)
        patients = cur.fetchall()
        cur.close()
        return patients
    except Exception as e:
        print(e)
    return None

@connect_db
def select_single_patient(conn, id:int):
    try:
        cur = conn.cursor()
        sql = 'select * from patinet where id = {}'.format(id)
        cur.execute(sql)
        patients = cur.fetchall()
        cur.close()
        patient = patients[0]
        return patient
    except Exception as e:
        print(e)
    return None