from config.db import connect_db
from typing import Dict, Any, List

@connect_db
def insert_signup(conn, user:str, passw:str, utype:str, fname:str, lname:str, cid:str) -> bool:
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO signup (username, password, user_type, firstname, lastname, cid) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (user, passw, utype, fname, lname, cid)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def update_signup(conn, id:int, details:Dict[str, Any]) -> bool:
    try:
        cur = conn.cursor()
        params = ['{} = %s'.format(key) for key in details.key()]
        values = tuple(details.values())
        sql = 'UPDATE signup SET {} where id = {}'.format(','.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_signup(conn, id) -> bool:
    try:
        cur = conn.cursor()
        sql = 'delete from signup where id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False