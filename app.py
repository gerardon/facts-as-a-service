# coding: utf-8
from random import randrange

from flask import Flask, render_template

f = open('facts.txt', 'r')
FACTS = f.readlines()
f.close()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', fact=random_fact())

@app.route('/api/')
def api():
    return random_fact()


def random_fact():
    return FACTS[randrange(len(FACTS))].decode('utf-8')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
