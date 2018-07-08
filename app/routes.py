from app import app

@app.route("/")
def index():
    return "Project 1: TODO"