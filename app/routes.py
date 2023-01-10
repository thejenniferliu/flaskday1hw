from app import app

from flask import render_template


@app.route('/')
def index():
    page_title = "Here is a link of my favorite basketball players."
    return render_template('index.html', page_title = page_title )


@app.route('/top5')
def Top5():
    players_title = "Warriors Repeat 2023"
    bball_list = ['Stephen Curry', 'Allen Iverson', 'Derrick Rose', 'Klay Thompson', 'Kwahi Leonard']
    return render_template('index2.html', players_title = players_title, bball_list= bball_list )
