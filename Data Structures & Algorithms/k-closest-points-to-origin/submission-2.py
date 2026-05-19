class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashMap = defaultdict(list)
        result = []
        minHeap = []
        distSet = set()
        for point in points:
            dist = (point[0])**2 + (point[1])**2
            hashMap[dist].append(point)
            if dist not in distSet:
                heapq.heappush(minHeap, dist)
                distSet.add(dist)
        
        while k:
            listOfPoints = hashMap.get(heapq.heappop(minHeap))
            if listOfPoints:
                for i in listOfPoints:
                    result.append(i)
                    k-=1
        return result