from flask import Blueprint
from Controllers.review_controller import create_review, get_all_reviews
from Middleware.middleware import jwt_required


review_bp = Blueprint('review_bp', __name__)

review_bp.route("/", methods=["Post"])(jwt_required(create_review))
review_bp.route("/", methods=["Get"])(jwt_required(get_all_reviews))