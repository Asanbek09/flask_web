from config.db import connect_db
from typing import Dict, Any

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