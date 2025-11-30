from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


# Greet routes
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


# Temperature conversion function (Celsius → Fahrenheit)
def c_to_f(celsius):
    return celsius * 9 / 5 + 32


# Route for temperature conversion
@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius_value = float(celsius)
        fahrenheit_value = c_to_f(celsius_value)
        return f"{celsius_value}°C is {fahrenheit_value}°F"
    except ValueError:
        return "Invalid temperature. Please enter a number."


if __name__ == '__main__':
    app.run()
