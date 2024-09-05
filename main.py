from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Product, Category  # Импорт моделей из папки app
from app.config import DATABASE_URI  # Импорт конфигурации из папки app

# Остальной код остается без изменений...


# Создаем движок для подключения к базе данных
engine = create_engine(DATABASE_URI, echo=True)

# Создаем все таблицы в базе данных (если их нет)
Base.metadata.create_all(engine)

# Создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Пример добавления данных в базу
new_category = Category(name='Electronics', description='Electronic items')
new_product = Product(name='Laptop', price=1500, in_stock=True, category=new_category)

# Добавляем объекты в сессию
session.add(new_category)
session.add(new_product)

# Сохраняем изменения в базе данных
session.commit()

# Выводим результаты
print(f"Added category: {new_category.name}, product: {new_product.name}")
