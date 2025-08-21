from app import db
from datetime import datetime



class Reviews(db.Model):
    __tablename__ = "reviews_table"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.String(50), nullable=False)
    rating=db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.Date, nullable=False)
    updated_at = db.Column(db.Date, nullable=False)
    deleted = db.Column(db.Boolean, nullable=False, default=False)  # default False if not provided
    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    def __repr__(self):
        return f"<Reviews {self.id}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "product_id": self.product_id,
            "rating": self.rating,
            "review": self.review,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }