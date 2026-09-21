class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = {0}
        stack = [(0, -1)]           

        while stack:
            node, par = stack.pop()
            for nei in adj[node]:
                if nei == par:
                    continue
                if nei in visit:  
                    return False
                visit.add(nei)
                stack.append((nei, node))

        return len(visit) == n
        