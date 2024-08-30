from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Задача 1: Создайте экземпляр движка для подключения к SQLite базе данных в памяти.
engine = create_engine('sqlite:///:memory:', echo=True)

# Задача 2: Создайте сессию для взаимодействия с базой данных, используя созданный движок.
Session = sessionmaker(bind=engine)
session = Session()

# Задача 3: Определите модель продукта Product.
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, default=True)

    # Задача 5: Установите связь между таблицами Product и Category.
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")


# Задача 4: Определите связанную модель категории Category.
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    products = relationship("Product", back_populates="category")


Base.metadata.create_all(engine)
