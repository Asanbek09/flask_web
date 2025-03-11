from flask import Flask

app = Flask(__name__, template_folder='pages')

@app.route('/', methods=['GET'])
def index():
    return "This is an online ... counseling system(OPCS)"

@app.route('/home', methods=['GET'])
def home():
    return ''''<html><head><title>Online Personal … System</title></head><body><h1>Online … Counseling System (OPCS)</h1>
    <p>This is a template of a web-based counseling
    application where counselors can … … …</em>
    </body></html>'''


@app.route('signup/form', methods=['GET'])
def signup_users_form():
    resp = Response(response= render_template('add_signup.html'), status=200, content_type="text.html")
    return resp

@app.route('/signup/submit', methods=['POST'])
def signup_users_submit():
    username = request.form['username']
    password = request.form['password']
    user_type = request.form['utype']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    cid = request.form['cid']
    insert_signup(username=username, passw=password, utype=user_type, fname=firstname, lname=lastname, cid=cid)
    return render_template('add_signup_submit.html', message='Add new user!'), 200

if __name__ == '__main__':
    app.run(debug=True)