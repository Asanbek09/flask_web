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