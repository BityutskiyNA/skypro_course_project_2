

class Pleer():

    def __init__(self, username):
        self.username = username
        self.used_words = []

    def return_len(self):
        return len(self.used_words)

    def add_words(self, word):
        self.used_words.append(word)

    def chec_word(self, word):
        if self.used_words.count(word) == 0:
            return False
        else:
            return True
