# coding: utf-8
from random import shuffle

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    f = open('facts.txt', 'r')
    facts = f.readlines()
    f.close()
    shuffle(facts)
    return render_template('home.html', fact=facts.pop())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
