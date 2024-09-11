from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import DATABASE_URI  # Импорт конфигурации базы данных
from app.routers.questions import questions_bp  # Импорт маршрутов (Blueprints)

app = Flask(__name__)

# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных и миграций
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорт моделей после инициализации базы данных
from app.models import *

# Импорт и регистрация маршрутов (Blueprints)
app.register_blueprint(questions_bp)

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)


