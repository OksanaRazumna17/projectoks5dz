from flask import Flask, jsonify, request
from app import app, db
from app.models import Category, Product

# Главная страница
@app.route('/')
def index():
    return "Welcome to the Product and Category API!"

# Маршрут для получения всех продуктов
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [{'id': p.id, 'name': p.name, 'price': str(p.price), 'in_stock': p.in_stock, 'category': p.category.name} for p in products]
    return jsonify(products_list)

# Маршрут для добавления продукта
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        price=data['price'],
        in_stock=data.get('in_stock', True),
        category_id=data['category_id']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added!'}), 201

# Маршрут для получения всех категорий
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    categories_list = [{'id': c.id, 'name': c.name, 'description': c.description} for c in categories]
    return jsonify(categories_list)

# Маршрут для добавления категории
@app.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()
    new_category = Category(name=data['name'], description=data['description'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added!'}), 201


