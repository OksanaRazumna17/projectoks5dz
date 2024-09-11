from flask import Blueprint, request, jsonify
from app import db
from app.models import Category

# Создаем Blueprint для маршрутов категорий
categories_bp = Blueprint('categories', __name__)

# Маршрут для создания новой категории
@categories_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()

    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_category = Category(name=data['name'], description=data.get('description'))
    db.session.add(new_category)
    db.session.commit()

    return jsonify({"message": "Category created!"}), 201
