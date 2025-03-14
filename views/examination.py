from __main__ import app
from flask import request, redirect, render_template, url_for, make_response
from services.utility import list_cid, list_pid, list_qid
from repository.question_details import insert_question_details
from services.patient_monitoring import record_patient_exam, list_passing_scores
from services.exam_management import add_exam_items, list_exam_details
from uuid import uuid4

@app.route('/exam/assign', methods=['GET', 'POST'])
def assign_exam():
    if request.method == 'GET':
        cids = list_cid()
        pids = list_pid()
        response = make_response(render_template('exam/assign_exam_form.html', pids=pids, cids=cids), 200)
        response.set_cookie('exam_token', str(uuid4()))
        return response, 200
    else:
        id = int(request.form['id'])
        cid = request.form['cid']
        pid = int(request.form['pid'])
        exam_date = request.form['exam_date']
        duration = int(request.form['duration'])
        result = insert_question_details(id=id, cid=cid, pid=pid, exam_date=exam_date, duration=duration)
        if result:
            task_token = request.cookies.get('exam_token')
            task = "exam assignment (task id {})".format(task_token)
            return redirect(url_for('redirect_success_exam', message=task))
        else:
            return redirect('/exam/task/error')

@app.route('/exam/score', methods=['GET', 'POST'])
def record_score():
    if request.method == 'GET':
        pids = list_pid()
        qids = list_qid()
        return render_template('exam/add_patient_score_form.html', pids=pids, qids=qids), 200
    else:
        params = dict()
        params['pid'] = int(request.form['pid'])
        params['qid'] = int(request.form['qid'])
        params['score'] = float(request.form['score'])
        params['total'] = float(request.form['total'])
        result = record_patient_exam(params)
        if result:
            task = "recording exam score"
            response = make_response()
            headers = dict()
            headers['Location'] = url_for('redirect_success_exam', message=task)
            response.headers = headers
            return response, 302
        else:
            return redirect('/exam/task/error')