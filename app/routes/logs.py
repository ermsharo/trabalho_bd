from flask import Blueprint, Response, jsonify, request
from datetime import datetime
import os
from dotenv import load_dotenv
import pandas as pd

from models import Insertion_log, Error_log, db
load_dotenv()

logs_route = Blueprint("LOG", __name__)



def create_insertion_log(data_dict):

    new_log = Insertion_log(
        env=data_dict.get("env"),
        table=data_dict.get('table'),
        log=data_dict.get('note'),
        created_at=datetime.utcnow(),
    )

    db.session.add(new_log)
    db.session.commit()

    return new_log

def create_error_log(data_dict):

    new_log = Error_log(
        env=data_dict.get("env"),
        route=data_dict.get('table'),
        log=data_dict.get('log'),
        created_at=data_dict.get('created_at'),
    )

    db.session.add(new_log)
    db.session.commit()

    return new_log

@logs_route.route("/log/insertion", methods=["POST"])
def inserion_logs():
    try:
        data = request.get_json()
        print("logs here",data, flush = True )
        
        # Iterate through the 'logs' list
        for log in data.get('logs', []):
            # Iterate through the keys and values in each log dictionary
            create_insertion_log(log)
            for key, value in log.items():
                print(f"{key}: {value}")
            print('-' * 50)  # Separator between logs
        
        return "Insert post log", 200

    except Exception as e:
        import traceback

        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    
@logs_route.route("/log/error", methods=["POST"])
def error_logs():
    try:
        data = request.get_json()
        print("logs here",data, flush = True )
        
        # Iterate through the 'logs' list
        for log in data.get('logs', []):
            # Iterate through the keys and values in each log dictionary
            create_error_log(log)
            for key, value in log.items():
                print(f"{key}: {value}")
            print('-' * 50)  # Separator between logs
        
        return "Insert error log", 200

    except Exception as e:
        import traceback

        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    

@logs_route.route("/logs/error/csv", methods=["GET"])
def error_to_csv_route():
    # Get all orders
    all_registers = Error_log.query.all()

    # Extract column names from the model
    column_names = [column.key for column in Error_log.__table__.columns]

    # Create a DataFrame from the orders
    all_registers_df = pd.DataFrame(
        [
            {col: getattr(register, col) for col in column_names}
            for register in all_registers
        ]
    )

    # Create a CSV string from the DataFrame
    csv_data = all_registers_df.to_csv(index=False)

    # Create a CSV response
    response = Response(
        csv_data,
        content_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=orders.csv",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )

    return response


@logs_route.route("/logs/insertion/csv", methods=["GET"])
def insert_to_csv_route():
    # Get all orders
    all_registers = Insertion_log.query.all()

    # Extract column names from the model
    column_names = [column.key for column in Insertion_log.__table__.columns]

    # Create a DataFrame from the orders
    all_registers_df = pd.DataFrame(
        [
            {col: getattr(register, col) for col in column_names}
            for register in all_registers
        ]
    )

    # Create a CSV string from the DataFrame
    csv_data = all_registers_df.to_csv(index=False)

    # Create a CSV response
    response = Response(
        csv_data,
        content_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=orders.csv",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )

    return response