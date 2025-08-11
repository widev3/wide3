from flask import Flask
from routes.mount import mount_bp

app = Flask(__name__)

app.register_blueprint(mount_bp, url_prefix="/mount")


if __name__ == "__main__":
    app.run(debug=True)
