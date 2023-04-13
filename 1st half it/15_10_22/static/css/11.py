from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tusk1')
def name():
    return render_template('tusk1.html')

if __name__ == "__main__":
    app.run()