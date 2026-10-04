from flask import Flask, jsonify


app = Flask(__name__)


def suma(a, b):
    return a + b


@app.route("/api")
def api():
    resultado = suma(2, 3)
    return jsonify({"result": resultado})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)