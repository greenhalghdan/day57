from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now()
    name = "Daniel Greenhalgh"
    return render_template("index.html", num=random_number, NAME=name, CURRENT_YEAR=year.year)


if __name__ == "__main__":
    app.run(debug=True)