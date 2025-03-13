from config.db import connect_db
from typing import Dict, Any, List
from datetime import date

@connect_db
def insert_user(conn, id:int, user:str, passw:str, user_approved:date) -> bool:
    try:
        cur = conn.cursor()
        sql = 'insert into users(id, username, password, user_approved) values (%s, %s, %s, %s)'
        values = (id, user, passw, user_approved)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def update_user(conn, id:int, details:Dict[str, Any]) ->bool:
    try:
        cur = conn.cursor()
        params = ['{} = %s'.format(key) for key in details.keys()]
        values = tuple(details.values())
        sql = 'update users set {} where id = {}'.format(', '.join(params), id)
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def delete_user(conn, id:int) -> bool:
    try:
        cur = conn.cursor()
        sql = 'delete from users where id = %s'
        values = (id, )
        cur.execute(sql, values)
        cur.close()
        return True
    except Exception as e:
        cur.close()
        print(e)
    return False

@connect_db
def select_all_user(conn) -> List[Any]:
    try:
        cur = conn.cursor()
        sql = 'select * from users'
        cur.execute(sql)
        users = cur.fetchall()
        cur.close()
        return users
    except Exception as e:
        print(e)
    return None

@connect_db
def select_single_user(conn, id:int) -> Any:
    try:
        cur = conn.cursor()
        sql = 'select * from users where id = {}'.format(id)
        cur.execute(sql)
        users = cur.fetchall()
        user = users[0]
        cur.close()
        return user
    except Exception as e:
        print(e)
    return None

@connect_db
def validate_user(conn, user, passwd) -> bool:
    try:
        cur = conn.cursor()
        sql = "select * from users where username = '{}' and password = '{}'".format(user, passwd)
        cur.execute(sql)
        users = cur.fetchall()
        cur.close()
        if len(users) > 0:
            return True
    except Exception as e:
        print(e)
    return False