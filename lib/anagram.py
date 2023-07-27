# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list_of_words):
        anagram_list = []
        for item in list_of_words:
            if len(self.word) == len(item) and sorted(self.word) == sorted(item):
                anagram_list.append(item)

        return anagram_list

        pass