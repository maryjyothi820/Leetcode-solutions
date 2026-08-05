1002. Find Common Characters.py
class Solution:
    def commonChars(self, words):
        freq = [100] * 26

        for word in words:
            temp = [0] * 26

            for ch in word:
                temp[ord(ch) - ord('a')] += 1

            for i in range(26):
                freq[i] = min(freq[i], temp[i])

        ans = []

        for i in range(26):
            while freq[i] > 0:
                ans.append(chr(i + ord('a')))
                freq[i] -= 1

        return ans
