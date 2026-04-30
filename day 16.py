139.word break
class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            if dp[i]:
                for word in wordDict:
                    wlen = len(word)

                    if i + wlen <= n:
                        match = True
                        k = 0

                        while k < wlen:
                            if s[i + k] != word[k]:
                                match = False
                                break
                            k += 1

                        if match:
                            dp[i + wlen] = True

        return dp[n]
140.word break 2
class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        memo = {}

        def dfs(index):
            if index in memo:
                return memo[index]

            if index == n:
                return [""]

            result = []

            for word in wordDict:
                wlen = len(word)

                if index + wlen <= n:
                    match = True
                    k = 0

                    while k < wlen:
                        if s[index + k] != word[k]:
                            match = False
                            break
                        k += 1

                    if match:
                        sub_sentences = dfs(index + wlen)

                        for sub in sub_sentences:
                            if sub == "":
                                result.append(word)
                            else:
                                result.append(word + " " + sub)

            memo[index] = result
            return result

        return dfs(0)