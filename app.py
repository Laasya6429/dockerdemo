from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def hello():
    return jsonify({"message": "Hello Devops"})

@app.route("/about")
def about():
    return jsonify({"message": "This is about page"})

@app.route("/contact")
def about():
    return jsonify({"message": "This is about contactpage"})

@app.route("/dashboard")
def about():
    return jsonify({"message": "This is dashboard"})


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)