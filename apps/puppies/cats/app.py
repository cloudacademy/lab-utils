import os
import random
import json
from flask import Flask, render_template
from flask import request


with open('cats.json') as data_file:
    quotes = json.load(data_file)

app = Flask(__name__)


@app.route('/cats')
def index():
    quote = quotes[random.randrange(len(quotes))]
    return render_template('index.html', quote=quote['quote'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
