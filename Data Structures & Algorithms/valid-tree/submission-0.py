class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = {0}
        stack = [0]
        while stack:
            for nei in adj[stack.pop()]:
                if nei not in visit:
                    visit.add(nei)
                    stack.append(nei)

        return len(visit) == n
        