from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route("/")
@app.route("/welcome_page")
def welcome_page():
    return render_template('welcome_page.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route('/xygrid')
def xygrid():
    return render_template('xy_grid.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
