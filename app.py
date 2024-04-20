from flask import Flask, render_template, request
from weather_app import get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_info = get_weather(city)
        if weather_info:
            return render_template('result.html', city=city, weather=weather_info['weather'], temp=weather_info['temp'])
        else:
            return render_template('result.html', city=city, error='City not found')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

