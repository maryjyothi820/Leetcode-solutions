39.combination sum
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        current = []

        def backtrack(start, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            i = start
            while i < len(candidates):
                current.append(candidates[i])
                backtrack(i, total + candidates[i])
                current.pop()
                i = i + 1

        backtrack(0, 0)
        return result
40.combination sum 2
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        current = []

        def backtrack(start, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            i = start
            while i < len(candidates):
                current.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                current.pop()

                i = i + 1
                while i < len(candidates) and candidates[i] == candidates[i - 1]:
                    i = i + 1

        backtrack(0, 0)
        return result