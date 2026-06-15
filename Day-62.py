3607:power-grid_maintainance.py
from collections import defaultdict
from bisect import bisect_left

class Solution:
    def processQueries(self, c, connections, queries):
        parent = list(range(c + 1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parent[py] = px
        # Build connected components
        for u, v in connections:
            union(u, v)
        groups = defaultdict(list)
        for i in range(1, c + 1):
            groups[find(i)].append(i)
        # Online status
        online = [True] * (c + 1)
        # Store active nodes in each component
        active = {}
        for root, nodes in groups.items():
            active[root] = sorted(nodes)
        answer = []
        for t, x in queries:
            if t == 1:
                if online[x]:
                    answer.append(x)
                else:
                    root = find(x)

                    if not active[root]:
                        answer.append(-1)
                    else:
                        answer.append(active[root][0])
            else:

                if online[x]:

                    online[x] = False

                    root = find(x)

                    idx = bisect_left(active[root], x)

                    if idx < len(active[root]) and active[root][idx] == x:
                        active[root].pop(idx)

        return answer
