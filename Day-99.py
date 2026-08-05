3138. Minimum Length of Anagram Concatenation.py
from collections import Counter

class Solution:
    def minAnagramLength(self, s):
        n = len(s)

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            target = Counter(s[:k])
            ok = True

            for i in range(k, n, k):
                if Counter(s[i:i+k]) != target:
                    ok = False
                    break

            if ok:
                return k

        return n
