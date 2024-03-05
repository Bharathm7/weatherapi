from flask import Flask, render_template
import pandas as pd;

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/<station>/<date>')
def api(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    result = {'station': station,
              'date': date,
              'temperature': temperature}
    return result

    app.run(debug=True, host='5000')
