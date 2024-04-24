import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from APP.models import db

# from routes.logs import logs_route
# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
# from run_updates import update_system_rt

load_dotenv()

app = Flask(__name__)

DB_STRING = os.getenv("DB_STRING")
# Update the SQLALCHEMY_DATABASE_URI with your PostgreSQL connection URL
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


@app.before_request
def authenticate_request():
    query_parameters = request.args
    print("query_parameters", query_parameters, flush=True)
    print("token", query_parameters.get("rt_token"), flush=True)


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
