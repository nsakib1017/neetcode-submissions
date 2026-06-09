class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        lastEnd = intervals[0][-1]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] >= lastEnd:
                lastEnd = intervals[i][1]
            else:
                count+=1
                lastEnd = min(intervals[i][1], lastEnd)
        return count

