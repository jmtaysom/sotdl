"""HTTP API endpoint"""
import random

from flask import Flask, jsonify, redirect, render_template, url_for
from ancestry import (
    Changeling,
    Clockwork,
    Dwarf,
    Faun,
    Goblin,
    Halfling,
    Human,
    Orc,
)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/random/')
def create_random():
    """Get a random character"""
    return redirect(url_for('create_{}'.format(random.choice((
        'changeling',
        'clockwork',
        'dwarf',
        'faun',
        'goblin',
        'halfling',
        'human',
        'orc',
    )))))


@app.route('/changeling/', defaults={'name': None})
@app.route('/changeling/<name>')
def create_changeling(name):
    return jsonify(Changeling(name).__dict__)


@app.route('/clockwork/', defaults={'name': None})
@app.route('/clockwork/<name>')
def create_clockwork(name):
    return jsonify(Clockwork(name).__dict__)


@app.route('/dwarf/', defaults={'name': None})
@app.route('/dwarf/<name>')
def create_dwarf(name):
    return jsonify(Dwarf(name).__dict__)


@app.route('/faun/', defaults={'name': None})
@app.route('/faun/<name>')
def create_faun(name):
    return jsonify(Faun(name).__dict__)


@app.route('/goblin/', defaults={'name': None})
@app.route('/goblin/<name>')
def create_goblin(name):
    return jsonify(Goblin(name).__dict__)


@app.route('/halfling/', defaults={'name': None})
@app.route('/halfling/<name>')
def create_halfling(name):
    return jsonify(Halfling(name).__dict__)


@app.route('/human/', defaults={'name': None})
@app.route('/human/<name>')
def create_human(name):
    return jsonify(Human(name).__dict__)


@app.route('/orc/', defaults={'name': None})
@app.route('/orc/<name>')
def create_orc(name):
    return jsonify(Orc(name).__dict__)


if __name__ == '__main__':
    app.run()
