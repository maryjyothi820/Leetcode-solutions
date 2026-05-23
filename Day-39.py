151.Reverse_words_in_a_string
class Solution:
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)