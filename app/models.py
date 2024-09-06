from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    # Отношение к продуктам, lazy=True означает, что продукты будут загружаться при доступе к ним
    products = db.relationship('Product', back_populates='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    in_stock = db.Column(db.Boolean, default=True)

    # Внешний ключ на категорию
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    # Связь с категорией, back_populates используется для двустороннего отношения
    category = db.relationship('Category', back_populates='products')


