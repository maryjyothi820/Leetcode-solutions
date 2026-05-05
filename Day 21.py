46.permutations
class Solution:
    def permute(self, nums):
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return

            i = 0
            while i < len(nums):
                if used[i] == False:
                    used[i] = True
                    current.append(nums[i])

                    backtrack()

                    current.pop()
                    used[i] = False

                i = i + 1

        backtrack()
        return result
47.permutations 2
class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return

            i = 0
            while i < len(nums):
                if used[i] == False:
                    # skip duplicates
                    if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                        i = i + 1
                        continue

                    used[i] = True
                    current.append(nums[i])

                    backtrack()

                    current.pop()
                    used[i] = False

                i = i + 1

        backtrack()
        return result