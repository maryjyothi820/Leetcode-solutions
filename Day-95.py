721. Accounts Merge.py
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px != py:
            self.parent[py] = px


class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        dsu = DSU(n)

        email_to_account = {}

        # Step 1: Union accounts sharing an email
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    dsu.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        # Step 2: Group emails by parent account
        groups = {}

        for email, idx in email_to_account.items():
            parent = dsu.find(idx)

            if parent not in groups:
                groups[parent] = []

            groups[parent].append(email)

        # Step 3: Build answer
        result = []

        for parent, emails in groups.items():
            result.append([accounts[parent][0]] + sorted(emails))

        return result
