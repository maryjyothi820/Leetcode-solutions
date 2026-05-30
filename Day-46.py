424.Longest_repeating_character_replacement.py
class Solution:
    def characterReplacement(self, s, k):
        d = {}
        left = 0
        maxf = 0
        ans = 0

        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0) + 1
            maxf = max(maxf, d[s[right]])

            while (right - left + 1) - maxf > k:
                d[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans