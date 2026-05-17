class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        stack = [self.root]
        for w in word:
            next_stack = []
            while stack:
                cur = stack.pop()
                if w == ".":
                    for child in cur.children.values():
                        next_stack.append(child)
                elif cur.children.get(w, 0):
                    next_stack.append(cur.children[w])
            stack = next_stack
            if not stack:
                return False
        return any(node.eow for node in stack)
            
