# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        pars = {}

        for i in range(n):
            m = len(accounts[i])

            pars[(accounts[i][0], i)] = (accounts[i][0], i)
            for j in range(1, m):
                pars[(accounts[i][j], -1)] = (accounts[i][j], -1)

        def find(node):
            while node != pars[node]:
                pars[node] = pars[pars[node]]
                node = pars[node]
            
            return node
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                if root1[1] == -1:
                    pars[root1] = root2
                else:
                    pars[root2] = root1
        
        for i in range(n):
            m = len(accounts[i])

            union((accounts[i][0], i), (accounts[i][1], -1))
            for j in range(1, m - 1):
                union((accounts[i][j], -1), (accounts[i][j + 1], -1))

        graph = defaultdict(list)

        for node in pars:
            root = find(node)

            if root != node:
                graph[root].append(node)
        
        result = []
        for node in graph:
            row = [node[0]]
            emails = [val[0] for val in graph[node] if val[0] != row[0]]
            emails.sort()
            row.extend(emails)

            result.append(row)

        return result
