class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0,ROWS - 1


        while top <= bottom:
            mid = top + (bottom-top) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
            
        if not (top <= bottom):
            return False
        
        row = (top + bottom)//2

        l,r = 0, COLS - 1

        while l <= r:
            mid = l + (r-l) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif  matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
       
        return False

