from flask import Flask, request, render_template
from color import getNewVals

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', redVal=127, greenVal=127, blueVal=127)


@app.route('/', methods=['POST'])
def read_form():
    data = request.form.get
    redVal = int(data('red'))
    greenVal = int(data('green'))
    blueVal = int(data('blue'))
    redValInc = int(data('redinc'))
    greenValInc = int(data('greeninc'))
    blueValInc = int(data('blueinc'))
    redValNew, greenValNew, blueValNew = getNewVals(redVal, greenVal, blueVal, redValInc, greenValInc, blueValInc)
    return render_template('index.html',
                           redVal=redVal, greenVal=greenVal, blueVal=blueVal,
                           redValInc=redValInc, greenValInc=greenValInc, blueValInc=blueValInc,
                           redValNew=redValNew, greenValNew=greenValNew, blueValNew=blueValNew)


app.run()
