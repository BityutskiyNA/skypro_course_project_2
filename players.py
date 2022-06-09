
class Pleer():

    def __init__(self, username):
        self.username = username
        self.used_words = set()

    def return_len(self):
        """
        Возвращает количестово эллемеентов в множестве used_words
        """
        return len(self.used_words)

    def add_words(self, word):
        """
        Функция добавляет слово в множество used_words
        """
        self.used_words.add(word)


    def check_word(self, word):
        """
        По заданию эта функция должна быть но так как хранение слов
        реализовал через множество необхдиость в ней не увидел,
        если нужно то доделаем.
        """
