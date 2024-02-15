from flask import Flask, render_template

app = Flask(__name__)


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

@app.route('/list')
def list_games():
    games = [
        Game('Tetris', 'Puzzle', 'Atari'),
        Game('God of War', 'Rock in Slash', 'PS2')
    ]

    return render_template('list.html', title='Games', games=games)


app.run(port=8080)
