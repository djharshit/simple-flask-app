from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home_page():
    return jsonify({"message": "Hello, World!"})


@app.route("/data", methods=["POST"])
def data():
    print(request.headers)
    print(request.args)
    print(request.form)

    return jsonify({"message": "Data received"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
