from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return render_template('list.html', title="Games")


app.run(port=8080)
