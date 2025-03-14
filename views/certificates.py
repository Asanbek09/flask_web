from __main__ import app
from datetime import date

@app.route('/certificate/accomp/<string:name>/<string:course>/<date:accomplished_date>')
def show_certification(name:str, course:str, accomplished_date:date):
    certificate = """
         <html>
            <head>
                <title>Certificate of Accomplishment</title>
            </head>
            <body>
                <h1>Certificate of Accomplishment</h1>
                <p>The participant {} is, hereby awarded this certificate of accomplishment
                in {} course on {} date for passing all exams. He/she proved to be ready for any of his/her future endeavors.</em>
            </body>
        </html>
    """.format(name, course, accomplished_date)
    return certificate, 200