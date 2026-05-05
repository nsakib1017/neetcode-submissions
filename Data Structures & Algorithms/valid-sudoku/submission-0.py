class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap_row = {i : set() for i in range(0,9)}
        hmap_col = {i : set() for i in range(0,9)}
        hmap_square = {i : set() for i in range(0,9)}

        valid = True

        for i in range (0,len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in hmap_row[i] or board[i][j] in hmap_col[j] or board[i][j] in hmap_square[i//3 * 3 + j//3]:
                        valid = False
                        break
                    else:
                        hmap_row[i].add(board[i][j])
                        hmap_col[j].add(board[i][j])
                        hmap_square[i//3 * 3 + j//3].add(board[i][j])
            if not valid:
                break
        return valid
                        
