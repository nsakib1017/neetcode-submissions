class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visiting, visited = set(), set()

        def dfs(crs):
            if crs in visiting:      # back edge -> cycle
                return False
            if crs in visited:       # already emitted
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output