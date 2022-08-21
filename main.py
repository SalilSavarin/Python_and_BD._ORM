import sqlalchemy
from sqlalchemy.orm import sessionmaker
from password_postgresql import password 

from models import create_tables, Publisher, Book, Shop, Stock, Sale



DSN = f'postgresql://postgres:{password}@localhost:5432/bookmarketdb'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher_1 = Publisher(id= 1, name='Stan Lee')
book_1 = Book(id=1, title='Spider-man: Freak! Public menace!', publisher= publisher_1)
book_2 = Book(id=2, title='Duel to the Death with the Vulture!', publisher= publisher_1)
# session.add_all([publisher_1, book_1, book_2])
# session.commit()
# print(publisher_1)
# print(book_1)
# print(book_2)
# for c in session.query(Publisher).filter(Publisher.id == 1).all():
#     print(c)

def search_publisher():
    while True:
        command = input('''
        i - поиск по id автора 
        n - поиск по имени автора 
        q - выход из программы
        ''')
        if command == 'q':
            print('Вы закрыли программу')
            break
        if command == 'i':
            inf_for_search= input('Введи id автора: ')
            for inf in session.query(Publisher).filter(Publisher.id == int(inf_for_search)).all():
                print(inf)
        if command == 'n':
            inf_for_search= input('Введи имя и фамилию автора : ')
            for c in session.query(Publisher).filter(Publisher.name.like(inf_for_search)).all():
                print(inf)
search_publisher()

session.close()
