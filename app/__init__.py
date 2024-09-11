from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import DATABASE_URI  # Убедитесь, что DATABASE_URI настроен в config.py

# Инициализация Flask приложения
app = Flask(__name__)

# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключаем слежение за изменениями для улучшения производительности

# Инициализация базы данных и миграций
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорт моделей после инициализации базы данных
from . import models

# Регистрация маршрутов (Blueprints)
from app.routers.categories import categories_bp  # Импортируем Blueprint для категорий

# Регистрируем Blueprint для категорий
app.register_blueprint(categories_bp)

if __name__ == '__main__':
    app.run(debug=True)

