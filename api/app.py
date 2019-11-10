from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>")
def home(name):
    return f"Welcome {name}"

app.run(debug=True)