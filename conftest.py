import pytest
from main import BooksCollector

@pytest.fixture
def collector_example():
    collector = BooksCollector()
    collector.books_genre = {'Томиэ': '',
                             '10 негритят': 'Детективы',
                             'Зодиак': 'Детективы',
                             'Остров сокровищ': 'Мультфильмы'}
    collector.favorites = ['Скитания Эманон', 'Скотный двор']
    return collector


