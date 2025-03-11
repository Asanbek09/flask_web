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


@app.route('signup/form', methods=['POST'])
def signup_users_form():
    resp = Response(response= render_template('add_signup.html'), status=200, content_type="text.html")
    return resp

if __name__ == '__main__':
    app.run(debug=True)