1443. Minimum Time to Collect All Apples in a Tree.py
from collections import defaultdict
class Solution:
    def minTime(self, n, edges, hasApple):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            total = 0
            for child in graph[node]:
                if child == parent:
                    continue
                child_time = dfs(child, node)
                if child_time > 0 or hasApple[child]:
                    total += child_time + 2
            return total
        return dfs(0, -1)
