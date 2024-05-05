import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from models import db


load_dotenv()

app = Flask(__name__)

DB_STRING = os.getenv("DB_STRING")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_STRING
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)

CORS(
    app,
    origins="*",
    methods="*",
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization", "test"],
)


@app.route("/")
def hello_world():
    print("Ola ", flush=True)
    return "Hello from or db project"


def main():
    app.app_context()
    app.run()


# Run the Flask application
if __name__ == "__main__":
    main()
