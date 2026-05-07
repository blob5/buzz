import os

from flask import Flask

from buzz import generator

app = Flask(__name__)


@app.route("/")
def generate_buzz():
    page = """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Buzz</title>
  <style>
    .gif-stage {
      height: 100vh;
      width: 100vw;
    }

    .gif-stage img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
  </style>
</head>
<body>
  <h1>"""
    page += generator.generate_buzz()
    page += """</h1>
  <section class=\"gif-stage\" aria-label=\"Fried fish sandwich gif\">
    <img src=\"https://rotatingsandwiches.com/wp-content/uploads/2024/12/fried-fish-sandwich-hanks.gif\" alt=\"Fried fish sandwich spinning\" />
  </section>
</body>
</html>"""
    return page


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
