from config.db import connect_db
from typing import Dict, Any
from datetime import date

@connect_db
def insert_question_choice(conn, qid:int, item_id:int, choice:str, choice_text:str, correct_choice:bool):
    try:
        cur = conn.cursor()
        sql = 'insert into question_choices (qid, item_id, choice, choice_text, correct_choice) values (%s, %s, %s, %s, %s)'
        values = (qid, item_id, choice, choice_text, correct_choice)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def update_question_choice(conn, id:int, details:Dict[str, Any]):
    try:
        cur = conn.cursor() 
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'update question_choices set {} where id = {}'.format(', '.join(params), id);
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False 

@connect_db
def delete_question_choice(conn, id:int):
    try:
        cur = conn.cursor() 
        sql = 'delete from question_choices where id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True 
    except Exception as e:
        cur.close()
        print(e)
    return False