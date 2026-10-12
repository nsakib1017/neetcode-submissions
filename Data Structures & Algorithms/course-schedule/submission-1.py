class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        unlocks = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            unlocks[pre].append(crs)
            indegree[crs] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0
        while q:
            cur = q.popleft()
            taken += 1
            for nxt in unlocks[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return taken == numCourses