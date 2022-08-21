import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key= True)
    name = sq.Column(sq.String(length=100), unique= True)

    def __str__(self):
        return f'PUBLISHER id - {self.id} : name - {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key= True)
    title = sq.Column(sq.String(length=100), unique= True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable= False)

    publisher = relationship(Publisher, backref='book')

    def __str__(self):
        return f'BOOK id - {self.id}: title - {self.title}: id_publisher - {self.id_publisher}'

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key= True)
    name = sq.Column(sq.String(length=100), unique= True)

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key= True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable= False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable = False)
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref='book')
    shop = relationship(Shop, backref='shop')

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key= True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    count = sq.Column(sq.Integer)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)

    stock = relationship(Stock, backref='stock')


def create_tables(engine):
    Base.metadata.create_all(engine)