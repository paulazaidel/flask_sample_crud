from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


games = [
        Game('Tetris', 'Puzzle', 'Atari'),
        Game('God of War', 'Rock in Slash', 'PS2')
    ]


@app.route('/')
def index():
    return render_template('list.html', title='Games', games=games)


@app.route('/new')
def new():
    return render_template('post.html', title='New Game')


@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    games.append(Game(name, category, console))

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'admin':
        return redirect('/')

    return redirect('/login')


app.run(port=8080, debug=True)
