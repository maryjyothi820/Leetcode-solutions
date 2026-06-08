898.Bitwise_ORs_of_Subarrays.py
class Solution:
    def subarrayBitwiseORs(self, arr):

        result = set()
        current = set()

        for num in arr:

            next_set = {num}

            for x in current:
                next_set.add(x | num)

            current = next_set
            result.update(current)

        return len(result)
1048.Longest_string_chain
class Solution:
    def longestStrChain(self, words):

        words.sort(key=len)

        dp = {}
        max_chain = 1

        for word in words:
            dp[word] = 1

            for i in range(len(word)):

                prev = word[:i] + word[i+1:]

                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)

            max_chain = max(max_chain, dp[word])

        return max_chain
