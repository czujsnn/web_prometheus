from flask import Flask
import socket
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app

app = Flask(__name__)


@app.route("/healthz")
def healthz():
    return f"you have hit '/healthz' from backend1 \n hostname is: {socket.gethostname()}"

@app.route("/")
def default():
    return f"you have hit '/' from backend1 \n hostname is: {socket.gethostname()}"

@app.route("/metrics")
def metrics():
    return f""

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)