from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({
        "service": "payments-status",
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)