907_.py
class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        left = [0] * n
        right = [0] * n
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                value, freq = stack.pop()
                count = count + freq
            left[i] = count
            stack.append((arr[i], count))
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                value, freq = stack.pop()
                count = count + freq
            right[i] = count
            stack.append((arr[i], count))
        answer = 0
        for i in range(n):
            answer = answer + (arr[i] * left[i] * right[i])
            answer = answer % MOD
        return answer
