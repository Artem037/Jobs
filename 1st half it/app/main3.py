from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def links():
    return render_template('links.html')


@app.route('/link_add')
def links_manage():
    return render_template('link_add.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
