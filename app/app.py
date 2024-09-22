from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Модель Category
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))

# Маршрут для главной страницы (GET /)
@app.route('/')
def index():
    return "Welcome to the API!"

# Маршрут для получения всех категорий (GET /categories)
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    categories_list = [{'id': c.id, 'name': c.name, 'description': c.description} for c in categories]
    return jsonify(categories_list), 200

# Маршрут для добавления новой категории (POST /categories)
@app.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()

    # Проверяем наличие обязательных полей
    if 'name' not in data or 'description' not in data:
        return jsonify({'error': 'Name and description are required'}), 400

    new_category = Category(name=data['name'], description=data['description'])
    db.session.add(new_category)
    db.session.commit()

    return jsonify({'message': 'Category added successfully!'}), 201

# Маршрут для обновления категории по ID (PUT /categories/<id>)
@app.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()

    # Проверяем наличие названия категории
    if 'name' not in data:
        return jsonify({'error': 'Category name is required'}), 400

    try:
        category = Category.query.get(id)
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        category.name = data['name']
        category.description = data.get('description', category.description)  # Обновляем описание, если оно есть
        db.session.commit()
        return jsonify({'message': 'Category updated!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Маршрут для удаления категории по ID (DELETE /categories/<id>)
@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    try:
        category = Category.query.get(id)
        if not category:
            return jsonify({'error': 'Category not found'}), 404

        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': f'Category {id} deleted!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)


