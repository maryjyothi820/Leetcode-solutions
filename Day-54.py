2439.Minimize_max_of_array
class Solution:
    def minimizeArrayValue(self, nums):

        prefix_sum = 0
        answer = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            # ceil average of prefix
            current_max = (prefix_sum + i) // (i + 1)

            answer = max(answer, current_max)

        return answer
2707.Extra_charecters_in_a_string
class Solution:
    def minExtraChar(self, s, dictionary):

        word_set = set(dictionary)
        n = len(s)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            # case 1: skip current character
            dp[i] = 1 + dp[i + 1]

            # case 2: try all words
            for j in range(i, n):
                if s[i:j+1] in word_set:
                    dp[i] = min(dp[i], dp[j+1])

        return dp[0]