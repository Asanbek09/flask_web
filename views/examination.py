from __main__ import app
from flask import request, redirect, render_template, url_for, make_response

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