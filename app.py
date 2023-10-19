from flask import Flask, request, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Database connection
DATABASE_URI = 'sqlite:///db001.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def upload_csv():
    try:
        # Check if the request contains files
        if not request.is_json:
            return jsonify({"error": "No JSON data provided"}), 400

            # Extract the JSON data from the request
        json_data = request.json

        # Check if 'files' key is in the JSON data
        if 'files' not in json_data:
            return jsonify({"error": "'files' key not found in JSON data"}), 400

        files = json_data['files']

        for file_info in files:
            file_path = file_info[0]
            table_name = file_info[1]
            header = file_info[2]

            # Process the CSV file
            data = pd.read_csv(file_path, names=header)

            # Here you can use additional_data for each file as needed
            data.to_sql(table_name, con=engine, if_exists='replace', index=False)

        session.commit()
        return jsonify({"message": "Data uploaded successfully"}), 200
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


if __name__ == '__main__':
    app.run()
