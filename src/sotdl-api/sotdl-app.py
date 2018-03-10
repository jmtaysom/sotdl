from flask import Flask
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


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/changeling')
def create_changeling():
    print(Changeling())
    a = str(Changeling())
    return a


if __name__ == '__main__':
    app.run()
