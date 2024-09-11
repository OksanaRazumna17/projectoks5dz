from flask import Blueprint, jsonify, request
from app import db
from app.models import Question, Category

# Создаем Blueprint для маршрутов
questions_bp = Blueprint('questions', __name__)

# Маршрут для получения всех вопросов
@questions_bp.route('/questions', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    result = [
        {
            'id': question.id,
            'title': question.title,
            'body': question.body,
            'category_id': question.category_id
        } for question in questions
    ]
    return jsonify(result), 200

# Маршрут для создания нового вопроса
@questions_bp.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()

    if 'title' not in data or 'body' not in data or 'category_id' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    new_question = Question(
        title=data['title'],
        body=data['body'],
        category_id=data['category_id']
    )

    db.session.add(new_question)
    db.session.commit()

    return jsonify({'message': 'Question created!'}), 201

# Маршрут для получения вопроса по ID
@questions_bp.route('/questions/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get(id)
    if question is None:
        return jsonify({'error': 'Question not found'}), 404

    result = {
        'id': question.id,
        'title': question.title,
        'body': question.body,
        'category_id': question.category_id
    }

    return jsonify(result), 200
