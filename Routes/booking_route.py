from flask import Blueprint
from Controllers.booking_controller import create_booking, get_all_bookings

booking_bp = Blueprint('booking_bp', __name__)

booking_bp.route("/", methods=["POST"])(create_booking)
booking_bp.route("/", methods=["GET"])(get_all_bookings)
