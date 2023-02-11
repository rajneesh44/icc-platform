import os
from flask import Flask
from dotenv import load_dotenv
from icc_session_interface import ICCSessionInterface
from blueprints import *
from core.db_manager import DBManager


load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('APP_SECRET')
app.session_interface = ICCSessionInterface()

@app.route('/test', methods=["GET"])
def test():
    return "Server is up and running"


def register_blueprints():
    blueprints = [
        auth_blueprint
    ]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

if __name__ == "__main__":
    DBManager.initialize_instance()
    register_blueprints()
    app.run(host="0.0.0.0", port=8080, debug=True)