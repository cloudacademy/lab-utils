from flask import Flask, render_template
import os
import random
import json


with open('dogs.json') as data_file:
    quotes = json.load(data_file)

app = Flask(__name__)


@app.route('/')
def index():
    quote = quotes[random.randrange(len(quotes))]
    if request.headers['Content-Type'] == 'text/plain':
        return "Quote: " + quote['quote']
    elif request.headers['Content-Type'] == 'application/json':
        return json.dumps(quote)
    return render_template('index.html', quote=quote['quote'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
