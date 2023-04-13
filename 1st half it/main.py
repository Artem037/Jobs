from flask import Flask,render_template, url_for
import os
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/hello/<name>/<int:user_id>")
def hello(name, user_id):
    #name = 'Антон'
    regards = {'p1':'умный', 'p2':'креативный', 'p3':'смелый'}
    return render_template('hello.html', user=name, data=regards, id=user_id)

@app.route("/dir")
def path_dir():
    return '<br>.join(os.listdir())'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('path_dir'))
    print(url_for('hello', name='Ivan', user_id=101,category='staf',gender='male', _external=True))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
