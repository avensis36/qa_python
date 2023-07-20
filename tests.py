import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_books_genre_true(self, collector_example):

        list_of_books = {'Томэ': '',
                         '10 негритят': 'Детективы',
                         'Зодиак': 'Детективы',
                         'Остров сокровищ': 'Мультфильмы'}

        assert collector_example.books_genre == list_of_books, 'dictionary items differ, must be the same'

    def test_favourites_true(self, collector_example):

        assert collector_example.favorites == ['Скитания Эманон', 'Скотный двор']

    def test_genre_true(self, collector_example):

        assert collector_example.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_true(self, collector_example):

        assert collector_example.genre_age_rating == ['Ужасы', 'Детективы']


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

    def test_set_book_genre_set_horror(self, collector_example):

        collector_example.set_book_genre('Томиэ', 'Ужасы')
        true_book_genre = {'Томиэ': 'Ужасы',
                           '10 негритят': 'Детективы',
                           'Зодиак': 'Детективы',
                           'Остров сокровищ': 'Мультфильмы'}

        assert true_book_genre == collector_example.books_genre

    def test_get_book_genre_detective_true(self, collector_example):

        assert collector_example.get_book_genre('10 негритят') == 'Детективы'

    def test_get_books_with_specific_genre_get_two_detective_books(self, collector_example):

        detective_books = collector_example.get_books_with_specific_genre('Детективы')

        assert len(detective_books) == 2

    def test_get_books_genre_get_4_books(self, collector_example):

        assert len(collector_example.get_books_genre()) == 4

    def test_get_books_for_children_get_treasure_island(self, collector_example):

        assert collector_example.get_books_for_children() == ['Остров сокровищ']

    def test_add_book_in_favorites_true(self, collector_example):

        collector_example.add_book_in_favorites('Томиэ')

        assert 'Томиэ' in collector_example.favorites

    def test_delete_book_from_favourites_true(self, collector_example):

        collector_example.delete_book_from_favorites('Скитания Эманон')

        assert 'Скитания Эманон' not in collector_example.favorites

    def test_get_list_of_favorites_books_true(self, collector_example):

        list_of_favorites = ['Скитания Эманон', 'Скотный двор']

        assert list_of_favorites == collector_example.get_list_of_favorites_books()


