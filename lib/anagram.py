# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, l):
        word_to_check = []
        word_list = sorted([letter for letter in self.word])
        
        for anagram in l:
            if word_list == sorted([letter for letter in anagram]):
                word_to_check.append(anagram)
        return word_to_check