from datetime import date

class AdminUser:
    id:int
    position:str
    age:int
    emp_date:date
    emp_status:str
    username:str
    password:str
    utype:int
    firstname:str
    lastname:str
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.position = kwargs.get('position', '')
        self.age = kwargs.get('age', 0)
        self.emp_date = kwargs.get('emp_date', None)
        self.emp_status = kwargs.get('emp_status', '')
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.utype = kwargs.get('utype', 0)
        self.firstname = kwargs.get('firstname', '')
        self.lastname = kwargs.get('lastname', '')

class CounselorUser:
    id:int
    age:int
    position:str
    prof_started:date
    username:str
    password:str
    utype:int
    firstname:str
    lastname:str
    cid:str
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.age = kwargs.get('age', 0)
        self.position = kwargs.get('position', '')
        self.prof_started = kwargs.get('prof_started', None)
        self.username = kwargs.get('username', '')
        self.password = kwargs.get('password', '')
        self.utype = kwargs.get('utype', 0)
        self.firstname = kwargs.get('firstname', '')
        self.lastname = kwargs.get('lastname', '')