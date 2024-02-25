from flask import flash, redirect, render_template, request, session, url_for


def login():
    redirect_page = request.args.get("redirect") or url_for("game.index")
    return render_template("login.html", redirect_page=redirect_page)


def authenticate():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin":
        session["username"] = username
        flash(f"Welcome {username}!")

        redirect_page = request.form["redirect_page"]
        return redirect(redirect_page)

    flash("User not found!")
    return redirect(url_for("auth.login"))


def logout():
    session["username"] = None

    flash("Logged out user!")
    return redirect(url_for("auth.login"))
