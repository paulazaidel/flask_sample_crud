from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = '67ea2d22-6820-47f0-b188-42d59a07aefb'


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
    if not session['username'] or 'username' not in session:
        return redirect(url_for('login', redirect=url_for('new')))
    return render_template('post.html', title='New Game')


@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    games.append(Game(name, category, console))

    return redirect(url_for('index'))


@app.route('/login')
def login():
    redirect_page = request.args.get('redirect') or url_for('index')
    return render_template('login.html', redirect_page=redirect_page)


@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'admin':
        session['username'] = username
        flash(f'Welcome {session['username']}!')

        redirect_page = request.form['redirect_page']
        return redirect(redirect_page)

    flash('User not found!')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['username'] = None

    flash('Logged out user!')
    return redirect(url_for('login'))


app.run(port=8080, debug=True)
