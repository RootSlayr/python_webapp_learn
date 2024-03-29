from flask import Flask

app = Flask(__name__)


@app.route("/hello")  # Add the decorator here
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
