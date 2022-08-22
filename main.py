import sqlalchemy
from sqlalchemy.orm import sessionmaker
from password_postgresql import password 

from models import Shop, create_tables, Publisher, Book, Stock, Sale



DSN = f'postgresql://postgres:{password}@localhost:5432/bookmarketdb'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher_1 = Publisher(id= 1, name='Stan Lee')
book_1 = Book(id=1, title='Spider-man: Freak! Public menace!', publisher= publisher_1)
book_2 = Book(id=2, title='Duel to the Death with the Vulture!', publisher= publisher_1)
shop_1 = Shop(id=1, name='OurGeekShop')
stock_1 = Stock(id=1, id_book=1, id_shop=1, count=3)
stock_2 = Stock(id=2, id_book=2, id_shop=1, count=4)
session.add_all([publisher_1,book_1,book_2,shop_1,stock_1,stock_2])
session.commit()


def search_publisher():
    while True:
        command = input('''
        i - поиск по id автора 
        n - поиск по имени автора (пример ввода: Joanne Rowling)
        q - выход из программы
        ''')

        if command == 'q':
            print('Вы закрыли программу')
            break

        if command == 'i':
            inf_for_search= input('Введи id автора: ')
            for inf in session.query(Publisher).filter(Publisher.id == int(inf_for_search)).all():
                print(inf)
            res_1 = session.query(Publisher, Book).join(Book).filter(Publisher.id == 1).all()
            list_book_id = []
            for pub, book in res_1:
                list_book_id.append(book.id)
            for id_book in list_book_id:
                res_2 = session.query(Stock).join(Book).filter(Stock.id_book == id_book).all()
                for stock in res_2:
                    id_shop = stock.id_shop
            for inf_shop in session.query(Shop).join(Stock).filter(Shop.id == id_shop).all():
                print(inf_shop)

        if command == 'n':
            inf_for_search= input('Введи имя и фамилию автора : ')
            for inf in session.query(Publisher).filter(Publisher.name.like(inf_for_search)).all():
                print(inf)
            res_1 = session.query(Publisher, Book).join(Book).filter(Publisher.id == 1).all()
            list_book_id = []
            for pub, book in res_1:
                list_book_id.append(book.id)
            for id_book in list_book_id:
                res_2 = session.query(Stock).join(Book).filter(Stock.id_book == id_book).all()
                for stock in res_2:
                    id_shop = stock.id_shop
            for inf_shop in session.query(Shop).join(Stock).filter(Shop.id == id_shop).all():
                print(inf_shop)


search_publisher()

session.close()
