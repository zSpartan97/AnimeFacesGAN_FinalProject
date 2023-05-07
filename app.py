from flask import Flask, render_template
import os
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/random-image")
def random_image():
    image_files = [f for f in os.listdir("static") if f.endswith(".png")]
    random_image = random.choice(image_files)
    return f'<img src="/static/{random_image}">'


if __name__ == "__main__":
    app.run()
