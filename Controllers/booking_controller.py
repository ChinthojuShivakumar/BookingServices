from flask import request, jsonify
from Modals.booking_modal import Booking
from extensions import db
from datetime import datetime

def create_booking():
    data = request.get_json()

    required_fields = [
        'user_id', 'product_id', 'total_price', 'original_price',
        'discount_amount', 'discount_percent', 'booking_date',
        'status', 'order_id', 'shipping_price', 'address_id', 'payment_mode'
    ]

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"success": False, "message": f"Missing fields: {', '.join(missing_fields)}"}), 400

    try:
        booking = Booking(
            user_id=data['user_id'],
            product_id=data['product_id'],
            total_price=data['total_price'],
            original_price=data['original_price'],
            discount_amount=data['discount_amount'],
            discount_percent=data['discount_percent'],
            booking_date=datetime.fromisoformat(data['booking_date']),
            status=data['status'],
            order_id=data['order_id'],
            shipping_price=data['shipping_price'],
            address_id=data['address_id'],
            payment_mode=data['payment_mode'],

            # Optional fields - check if provided, else None
            delivered_at=datetime.fromisoformat(data['delivered_at']) if data.get('delivered_at') else None,
            cancelled_at=datetime.fromisoformat(data['cancelled_at']) if data.get('cancelled_at') else None,
            shipped_at=datetime.fromisoformat(data['shipped_at']) if data.get('shipped_at') else None,
            returned_at=datetime.fromisoformat(data['returned_at']) if data.get('returned_at') else None,
            deleted=data.get('deleted', False),
            deleted_at=datetime.fromisoformat(data['deleted_at']) if data.get('deleted_at') else None,
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else datetime.utcnow(),
            updated_at=datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else datetime.utcnow(),
        )

        db.session.add(booking)
        db.session.commit()

        return jsonify({"success": True, "data": booking.serialize()}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500


def get_all_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([b.serialize() for b in bookings]), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
