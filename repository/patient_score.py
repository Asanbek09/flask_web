from config.db import connect_db
from typing import Dict, Any

@connect_db
def insert_patient_score(conn, pid:int, qid:int, score:float, total:float, status:str, percentage:float):
    try:
        cur = conn.cursor()
        sql = 'insert into patient_score(pid, qid, score, total, status, percentage) values (%s, %s,  %s, %s, %s, %s)'
        values = (pid, qid, score, total, status, percentage)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def update_patient_score(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor()
        params = ['{} = %s'.format(key) for key in details.key()]
        values = tuple(details.values())
        sql = 'update patient_score set {} where id = {}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_patient_score(conn, id:int):
    try:
        cur = conn.cursor()
        sql = 'delete from patient_score where id = %s'
        values =(id, )
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_patient_score(conn):
    try:
        cur = conn.cursor()
        sql = 'select * from patient_score'
        cur.execute(sql)
        scores = cur.fetchall()
        cur.close()
        return scores
    except Exception as e:
        print(e)
    return None

@connect_db
def select_single_patient_score(conn, id:int):
    try:
        cur = conn.cursor()
        sql = 'select * from patient_score whhre id = {}'.format(id)
        cur.execute(sql)
        scores = cur.fetchall()
        score = scores[0]
        return score
    except Exception as e:
        print(e)
    return None

def record_patient_exam(formdata:Dict[str, Any]) -> bool:
    try:
        pct = round((formdata['score'] / formdata['total']) * 100, 2)
        status = None
        if (pct >= 70):
            status = 'passed'
        elif (pct < 70) and (pct >= 55):
            status = 'conditional'
        else:
            status = 'failed'
        insert_patient_score(pid=formdata['pid'], qid=formdata['qid'], score=formdata['score'], total=formdata['total'], status=status, percentage=pct)
        return True
    except Exception as e:
        print(e)
    return False