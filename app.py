from flask import Ｆlask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return  "<p>Hello, world!</p>"