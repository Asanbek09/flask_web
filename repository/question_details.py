from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_question_details(conn, id:int, cid:str, pid:int, exam_date:date, duration:int):
    try:
        cur = conn.cursor()
        sql = 'insert into question_details (id, cid, pid, exam_date, duration) values (%s, %s, %s, %s, %s)'
        values = (id, cid, pid, exam_date, duration)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def update_question_details(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor()
        params = ['{} = %s'.format(key) for key in details.key()]
        values = tuple(details.values())
        sql = 'update question_details set {} where id = {}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_question_details(conn, id:int):
    try:
        cur = conn.cursor()
        sql = 'delete from question_details where id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False