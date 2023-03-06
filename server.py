import os

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return f'''
    <h2>Карсота</h2>
    <p>
    <img src="{url_for('static', filename='img/3.jpeg')}"
     width="600" alt="красота страшная сила">
     </p>
     <h2>Карсота</h2>
    <p>
     <p>
<img src="{url_for('static', filename='img/2.jpeg')}"
     width="600" alt="красота страшная сила">
     </p>'''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)