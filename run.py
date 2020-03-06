from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json().values()
    return render_template('idr_rates.html', datas= json_data)


if __name__ == '__main__':
    app.run(debug=True)