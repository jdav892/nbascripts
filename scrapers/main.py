from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "<h1>NBA Stat Leaders</h1>"

@app.route("/scoring")
def ppg_post():
    return

@app.route("/assists")
def apg_post():
    return 

@app.route("/steals")
def spg_post():
    return 

@app.route("/rebounds")
def rbpg_post():
    return 

@app.route("/blocks")
def bpg_post():
    return 


if __name__ == "__main__":
    app.run(debug=True)

    
