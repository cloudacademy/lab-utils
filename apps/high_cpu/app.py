from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/burn-baby-burn')
def burn_baby_burn():
    try:
        os.system("yes > /dev/null & yes > /dev/null & yes > /dev/null &")
        burn = True
        message = 'Burn Baby Burn!'
    except:
        burn = False
        message = 'Something went wrong'
    return render_template('burn-baby-burn.html', burn=burn, message=message)

@app.route('/relax')
def relax():
    try:
        os.system("killall yes")
        burn = True
        message = 'This are better now...'
    except:
        burn = False
        message = 'Something went wrong'
    return render_template('relax.html', burn=burn, message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
