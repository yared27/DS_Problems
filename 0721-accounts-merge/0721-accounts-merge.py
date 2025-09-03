class UnionFind:
    def __init__(self,n):
        self.root = {i : i for i in range(n)}
        self.rank = [0]*n

    def find(self, x):
            while x != self.root[x]:
                self.root[x] = self.root[self.root[x]]
                x = self.root[x]
            return self.root[x]
        
    def union(self, x, y):
        xroot  = self.find(x)
        yroot = self.find(y)

        if yroot != xroot:
            if self.rank[xroot] > self.rank[yroot]:
                self.root[yroot] = xroot
            elif self.rank[yroot] > self.rank[xroot]:
                self.root[xroot] = yroot
            else:
                self.root[xroot] = yroot
                self.rank[yroot] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = dict()

        for accountId, accountData in enumerate(accounts):
            for j in range(1, len(accountData)):
                email = accountData[j]
                if email in emailToAccount:
                    uf.union(accountId, emailToAccount[email])
                else:
                    emailToAccount[email] = accountId

        groupByAccount = defaultdict(list)
        for email, accountId in emailToAccount.items():
            mainAccountId = uf.find(accountId)
            groupByAccount[mainAccountId].append(email)

        res = []
        for accountId, emails in groupByAccount.items():
            data = [accounts[accountId][0]]
            data.extend(sorted(emails))
            res.append(data)
        return res