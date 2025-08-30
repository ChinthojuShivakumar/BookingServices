import jwt
from functools import wraps
from flask import request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()  

JWT_SECRET = os.getenv("JWT_SECRET")  # The secret or public key used to verify the JWT signature
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")  # Usually HS256 or RS256

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", None)
        if not auth_header:
            return jsonify({"success": False, "message": "Missing Authorization header"}), 401
        
        parts = auth_header.split()
        if parts[0].lower() != "bearer" or len(parts) != 2:
            return jsonify({"success": False, "message": "Authorization header must be Bearer token"}), 401
        
        token = parts[1]

        try:
            # Decode & verify the JWT token
            payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            # Optionally, you can attach user info to request context here
            request.user = payload
        except jwt.ExpiredSignatureError:
            return jsonify({"success": False, "message": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"success": False, "message": "Invalid token"}), 401
        
        return f(*args, **kwargs)
    return decorated
