

class Question:
    def __init__(self, original_word, allowed_subwords):
        self.original_word = original_word
        self.allowed_subwords = allowed_subwords

    def test_words(self, word):
        try:
            self.allowed_subwords.index(word)
            return True
        except Exception:
            return False

    def len_allowed_subwords(self):
        return len(self.allowed_subwords)
