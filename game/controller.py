from flask import render_template, request, redirect, session, url_for

from extensions import db
from models.game import Game


def index():
    games = Game.query.all()
    return render_template('list.html', title='Games', games=games)


def new():
    if not session['username'] or 'username' not in session:
        return redirect(url_for('auth.login', redirect=url_for('game.new')))
    return render_template('post.html', title='New Game')


def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)
    db.session.add(game)
    db.session.commit()

    return redirect(url_for('game.index'))
