from flask import Flask
import socket

app = Flask(__name__)


@app.route("/healthz")
def healthz():
    return f"you have hit '/healthz' from backend2 \n hostname is: {socket.gethostname()}"

@app.route("/")
def default():
    return f"you have hit '/' from backend2 \n hostname is: {socket.gethostname()}"

@app.route("/metrics")
def metrics():
    return f"Metric page for prometheus"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)