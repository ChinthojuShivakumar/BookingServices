from flask import Blueprint
from Controllers.review_controller import create_review, get_all_reviews


review_bp = Blueprint('review_bp', __name__)

review_bp.route("/", methods=["Post"])(create_review)
review_bp.route("/", methods=["Get"])(get_all_reviews)