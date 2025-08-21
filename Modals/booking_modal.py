from app import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = "booking_table"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.String(100), nullable=False)  # Changed to string to match schema
    total_price = db.Column(db.Integer, nullable=False)
    original_price = db.Column(db.Integer, nullable=False)
    discount_amount = db.Column(db.Integer, nullable=False)
    discount_percent = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)  # Date only
    status = db.Column(db.String, nullable=False, default="Pending")
    created_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    delivered_at = db.Column(db.Date, nullable=True)
    cancelled_at = db.Column(db.Date, nullable=True)
    shipped_at = db.Column(db.Date, nullable=True)
    returned_at = db.Column(db.Date, nullable=True)
    deleted = db.Column(db.Boolean, nullable=False, default=False)
    deleted_at = db.Column(db.Date, nullable=True)
    order_id = db.Column(db.String(50), nullable=False)
    shipping_price = db.Column(db.Integer, nullable=False)
    address_id = db.Column(db.Integer, nullable=False)
    payment_mode = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f"<Booking {self.id}>"

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "total_price": self.total_price,
            "original_price": self.original_price,
            "discount_amount": self.discount_amount,
            "discount_percent": self.discount_percent,
            "booking_date": self.booking_date.isoformat() if self.booking_date else None,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "delivered_at": self.delivered_at.isoformat() if self.delivered_at else None,
            "cancelled_at": self.cancelled_at.isoformat() if self.cancelled_at else None,
            "shipped_at": self.shipped_at.isoformat() if self.shipped_at else None,
            "returned_at": self.returned_at.isoformat() if self.returned_at else None,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
            "order_id": self.order_id,
            "shipping_price": self.shipping_price,
            "address_id": self.address_id,
            "payment_mode": self.payment_mode,
        }
