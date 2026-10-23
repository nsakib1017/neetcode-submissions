class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

    def addWord(self, word):
        curr = self
        for c in word:
            if not c in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(0,1), (0,-1),(1,0),(-1,0)]
        ROWS,COLS = len(board), len(board[0])
        result, visited = set(), set()

        root = TrieNode()

        for w in words:
            root.addWord(w)

        def backtrack(r,c,node,word):
            if 0<=r<ROWS and 0<=c<COLS and (r,c) not in visited and board[r][c] in node.children :
                visited.add((r,c))
                node = node.children[board[r][c]]
                word +=board[r][c]
                
                if node.eow:
                    result.add(word)

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    backtrack(nr, nc, node, word)
                visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r,c,root,"")
        return list(result)    
