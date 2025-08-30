import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from Routes.booking_route import booking_bp
from Routes.review_route import review_bp
from dotenv import load_dotenv
import os

load_dotenv()  # ✅ This loads variables from .env into environment


app = Flask(__name__)
# ✅ Read env variables
host = os.getenv("HOST_NAME")
port = os.getenv("PORT")
user = os.getenv("NAME")
password = os.getenv("PASSWORD")

# print(f"{user}:{password}@{host}:{port}")
# PostgreSQL config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:Pinky@143@localhost:5432/Booking Service'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/Booking Service'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(booking_bp, url_prefix='/bookings') 
app.register_blueprint(review_bp, url_prefix='/reviews') 

@app.route("/")
def home():
    return {"message": "Booking Service running with Flask + venv!"}

if __name__ == "__main__":
    app.run(debug=True, port=6061)
