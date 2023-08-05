from flask import Flask, render_template
import random
import datetime
import requests

GENDERURL = "https://api.genderize.io?"
AGEURL = "https://api.agify.io?"

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now()
    name = "Daniel Greenhalgh"
    return render_template("index.html", num=random_number, NAME=name, CURRENT_YEAR=year.year)


@app.route('/guess/<guess_name>')
def guess(guess_name):
    name = guess_name
    params = {
        "name": name
    }
    genderresponse = requests.get(url=GENDERURL, params=params)
    gender = genderresponse.json()
    ageresponse = requests.get(url=AGEURL, params=params)
    age = ageresponse.json()
    return render_template("guess.html", name=name.title(), GENDER=gender["gender"], AGE=age["age"])

@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)