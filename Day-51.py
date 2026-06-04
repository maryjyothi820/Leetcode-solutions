240.search_a_2D_matrix ||
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        row = 0
        col = n - 1  # start from top-right

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
2222.No_of_ways_to_select_buildings
class Solution:
    def numberOfWays(self, s):
        left0 = left1 = 0
        right0 = s.count('0')
        right1 = s.count('1')

        ans = 0

        for ch in s:
            if ch == '0':
                right0 -= 1
                ans += left1 * right1
                left0 += 1
            else:
                right1 -= 1
                ans += left0 * right0
                left1 += 1

        return ans