from flask import Flask
from extensions import db
from flask_sqlalchemy import SQLAlchemy
from Routes.booking_route import booking_bp
from Routes.review_route import review_bp

app = Flask(__name__)


# PostgreSQL config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:Pinky@143@localhost:5432/Booking Service'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pinky%40143@localhost:5432/Booking Service'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(booking_bp, url_prefix='/bookings') 
app.register_blueprint(review_bp, url_prefix='/reviews') 

@app.route("/")
def home():
    return {"message": "Booking Service running with Flask + venv!"}

if __name__ == "__main__":
    app.run(debug=True)
