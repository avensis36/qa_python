import pytest
from main import BooksCollector


class TestBooksCollector:

    list_of_books = ['Мечта на поражение',
                     'Дорохедоро',
                     'Компромисс']
    @pytest.mark.parametrize('name', list_of_books)
    def test_add_new_book_three_books(self, name):

        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book('Book 2')
        collector.add_new_book('Book 3')

        assert len(collector.books_genre) == 3

    def test_set_book_genre_set_horror(self):

        collector = BooksCollector()
        collector.books_genre = {'Томиэ': ''}
        collector.set_book_genre('Томиэ', 'Ужасы')

        assert collector.get_book_genre('Томиэ') == 'Ужасы'

    def test_get_book_genre_detective_true(self):

        collector = BooksCollector()
        collector.books_genre = {'10 негритят': 'Детективы'}
        detective_genre = 'Детективы'

        assert collector.get_book_genre('10 негритят') == detective_genre

    def test_get_books_with_specific_genre_get_two_detective_books(self):

        collector = BooksCollector()
        collector.books_genre = {'10 негритят': 'Детективы',
                                 'Зодиак': 'Детективы'}

        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_genre_get_4_books(self):

        collector = BooksCollector()
        collector.books_genre = {'Томиэ': '',
                                 '10 негритят': 'Детективы',
                                 'Зодиак': 'Детективы',
                                 'Остров сокровищ': 'Мультфильмы'}
        len_of_books_genre = 4

        assert len(collector.get_books_genre()) == len_of_books_genre

    def test_get_books_for_children_get_treasure_island(self):

        collector = BooksCollector()
        collector.books_genre = {'Остров сокровищ': 'Мультфильмы'}
        book_for_children = ['Остров сокровищ']

        assert collector.get_books_for_children() == book_for_children

    def test_add_book_in_favorites_true(self):

        collector = BooksCollector()
        collector.books_genre = {'Томиэ': ''}
        collector.add_book_in_favorites('Томиэ')

        assert 'Томиэ' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favourites_true(self):

        collector = BooksCollector()
        collector.books_genre = {'Томиэ': ''}
        collector.add_book_in_favorites('Томиэ')
        collector.delete_book_from_favorites('Томиэ')

        assert 'Томиэ' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_true(self):

        collector = BooksCollector()
        collector.books_genre = {'Томиэ': '',
                                 'Остров сокровищ': 'Мультфильмы'}
        collector.add_book_in_favorites('Томиэ')
        collector.add_book_in_favorites('Остров сокровищ')
        list_of_favorites = ['Томиэ', 'Остров сокровищ']

        assert list_of_favorites == collector.get_list_of_favorites_books()


