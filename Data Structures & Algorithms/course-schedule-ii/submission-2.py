class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegrees[crs]+=1
        
        q = deque()

        for crs in range(numCourses):
            if indegrees[crs]==0:
                q.append(crs)
        
        output = []
        finish = 0

        while q:
            crs = q.popleft()
            output.append(crs)
            finish+=1

            for nei in adj[crs]:
                indegrees[nei]-=1
                if indegrees[nei]==0:
                    q.append(nei)
        
        if finish!=numCourses:
            return []
        return output
