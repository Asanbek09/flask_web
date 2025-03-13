from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_question_pool(conn, qid:int, question:str, type:int):
    try:
        cur = conn.cursor()
        sql = 'insert into question_pool (qid, question, type) values (%s, %s, %s)'
        values = (qid, question, type)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def update_question_pool(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor()
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'update question_pool set {} where id = {}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_question_pool(conn, id:int):
    try:
        cur = conn.cursor()
        sql = 'delete from question_pool where id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False