import os
from flask import Flask, send_file
from flask_cors import CORS
from dotenv import load_dotenv
from icc_session_interface import ICCSessionInterface
from blueprints import *
from core.db_manager import DBManager


load_dotenv()

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = os.getenv('APP_SECRET')
app.session_interface = ICCSessionInterface()

@app.route('/test', methods=["GET"])
def test():
    return "Server is up and running"

@app.route('/test2', methods=["GET"])
def test2():
    return "Server is up and running! Again"

@app.route("/.well-known/pki-validation/70ACB4A7476CE024E4B77E5A095916A6.txt")
def render_file():
    return send_file("70ACB4A7476CE024E4B77E5A095916A6.txt")


def register_blueprints():
    blueprints = [
        auth_blueprint, user_blueprint, match_blueprint, product_blueprint,
        cart_blueprint, address_blueprint, utils_blueprint, order_blueprint,
        videos_blueprint
    ]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

if __name__ == "__main__":
    DBManager.initialize_instance()
    register_blueprints()
    app.run(host="0.0.0.0", port=8080, debug=True)