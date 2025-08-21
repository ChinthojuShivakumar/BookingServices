from flask import request, jsonify
from Modals.review_modal import Reviews
from extensions import db
from datetime import datetime



def create_review():
    data = request.get_json()

    required_fields = [
        'user_id', 'product_id', "rating", "review", "created_at", "updated_at", "deleted", "deleted_at"
    ]

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"success": False, "message": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        reviews = Reviews(
            user_id=data['user_id'],
            product_id=data['product_id'],
            rating=data['rating'],
            review=data["review"],

            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else datetime.utcnow(),
            updated_at=datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else datetime.utcnow(),
        )

        db.session.add(reviews)
        db.session.commit()

        return jsonify({"success": True, "data": reviews.serialize()}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500


def get_all_reviews():
    try:
        reviews = Reviews.query.all()
        return jsonify({"success": False, "reviews_list": [b.serialize() for b in reviews]}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500