from flask import Flask,render_template
import requests

app = Flask(__name__)

URL = "https://api.npoint.io/10a6861f75ce7cd2879c"
posts = requests.get(URL).json()


@app.route("/")
def home():
    return render_template("index.html", all_posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_posts in posts:
        if blog_posts["id"] == index:
            requested_post = blog_posts
    return render_template("post.html", post= requested_post)


if __name__=="__main__":
    app.run(debug= True)

