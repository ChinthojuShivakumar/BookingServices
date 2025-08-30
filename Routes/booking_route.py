from flask import Blueprint
from Controllers.booking_controller import create_booking, get_all_bookings
from Middleware.middleware import jwt_required

booking_bp = Blueprint('booking_bp', __name__)

booking_bp.route("/", methods=["POST"])(jwt_required(create_booking))
booking_bp.route("/", methods=["GET"])(jwt_required(get_all_bookings))
