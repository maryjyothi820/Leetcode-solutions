863. All Nodes Distance K in Binary Tree.py
from collections import deque

class Solution:
    def distanceK(self, root, target, k):

        parent = {}

        def dfs(node, par):
            if not node:
                return

            parent[node] = par

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        q = deque([target])
        visited = {target}
        distance = 0

        while q:

            if distance == k:
                return [node.val for node in q]

            for _ in range(len(q)):
                node = q.popleft()

                for nxt in (node.left, node.right, parent[node]):

                    if nxt and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)

            distance += 1

        return []
