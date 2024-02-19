from flask import render_template, request, redirect, session, flash, url_for

from db import games
from models.game import Game


def index():
    return render_template('list.html', title='Games', games=games)


def new():
    if not session['username'] or 'username' not in session:
        return redirect(url_for('auth.login', redirect=url_for('game.new')))
    return render_template('post.html', title='New Game')


def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    games.append(Game(name, category, console))

    return redirect(url_for('game.index'))
