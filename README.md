# Список реализованных тестов

Тест для метода `add_new_book`, который проверяет, что добавились именно три книги:  
`test_add_new_book_three_books`

Тест для метода `set_book_genre`, который проверяет, что для выбранной книги установлен жанр `'Ужасы'`:  
`test_set_book_genre_set_horror`

Тест для метода `get_book_genre`, который проверяет, что по названию выбранной книги возвращается её жанр:  
`test_get_book_genre_detective_true`

Тест для метода `get_books_with_specific_genre`, который проверяет, что длина списка книг по выбранному жанру равна двум:  
`test_get_books_with_specific_genre_get_two_detective_books`

Тест для метода `get_books_genre`, который проверяет, что длина поля `books_genre` равна четырем:  
`test_get_books_genre_get_4_books`

Тест для метода `get_books_for_children`, который проверяет, что возвращается единственная детская книга:  
`test_get_books_for_children_get_treasure_island`

Тест для метода `add_book_in_favorites`, который проверяет, что выбранная книга добавляется в список избранных книг:  
`test_add_book_in_favorites_true`

Тест для метода `delete_book_from_favourites`, который проверяет, что выбранная книга удаляется из списка избранных книг:  
`test_delete_book_from_favourites_true`

Тест для метода `get_list_of_favorites_books`, который проверяет, что возвращается список избранных книг:  
`test_get_list_of_favorites_books_true`