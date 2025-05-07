from flask import Flask, render_template, request
from src.predict import predict_fire
from src.weather_api import fetch_weather_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temp'])
        RH = float(request.form['rh'])
        wind = float(request.form['wind'])
        rain = float(request.form['rain'])
        result = predict_fire(temp, RH, wind, rain)
        return render_template('index.html', result=result)
    except:
        return render_template('index.html', result="Invalid input.")

@app.route('/predict_live', methods=['POST'])
def predict_live():
    try:
        temp, RH, wind, rain = fetch_weather_data()
        result = predict_fire(temp, RH, wind, rain)
        return render_template('index.html', result=f"{result} ({temp}°C, {RH}% RH, {wind} m/s, {rain} mm)")
    except Exception as e:
        return render_template('index.html', result=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
