from flask import Flask

app=Flask(__name__)

@app.route("/")
def blog():
    return "blog"
from mode_admin import ad

app.register_blueprint(ad)