from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/add_numbers")
def add_numbers():
    return render_template("add_numbers.html")


@app.route("/calculate", methods=["POST"])
def calculate_sum():
    print(request.data)
    print(request.args.get("num1"))
    num_1 = int(request.form["num1"])
    num_2 = int(request.form["num2"])
    print(num_1, num_2)
    ans = num_1 + num_2
    # print(ans)
    return render_template("add_numbers.html", result=ans)


if __name__ == "__main__":
    app.run(debug=True)
