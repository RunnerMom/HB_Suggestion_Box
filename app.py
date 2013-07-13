from flask import Flask, render_template, request, redirect
import model
import datetime

app = Flask(__name__)

@app.route("/")
def main():
    model.connect_to_db()
    posts = model.get_all_posts()
    return render_template("index.html", posts = posts)


@app.route("/add_post")
def add_post():
    model.connect_to_db()
    title = request.args.get("title")
    body = request.args.get("body")
    author = request.args.get("author")
    timestamp = datetime.datetime.now()
    post = model.Post(title, body, author, timestamp)
    post.add_post_to_db()

    return main()

if __name__ == "__main__":
    app.run(debug=True)
