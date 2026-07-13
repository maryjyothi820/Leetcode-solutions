599. Minimum Index Sum of Two Lists.py
class Solution:
    def findRestaurant(self, list1, list2):

        index_map = {}

        for i in range(len(list1)):
            index_map[list1[i]] = i

        ans = []
        min_sum = float('inf')

        for j in range(len(list2)):

            if list2[j] in index_map:

                total = j + index_map[list2[j]]

                if total < min_sum:
                    min_sum = total
                    ans = [list2[j]]

                elif total == min_sum:
                    ans.append(list2[j])

        return ans
