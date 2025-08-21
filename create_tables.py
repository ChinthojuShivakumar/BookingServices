from app import app
from extensions import db
from Modals.booking_modal import Booking
from Modals.review_modal import Reviews

with app.app_context():
    db.create_all()
    print("Tables Created Successfully!")