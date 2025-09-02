import sys

sys.dont_write_bytecode = True

from flask import Flask
from mount import mount_bp
from session import session_bp

app = Flask(__name__)

app.register_blueprint(session_bp, url_prefix="/session")
app.register_blueprint(mount_bp, url_prefix="/mount")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
