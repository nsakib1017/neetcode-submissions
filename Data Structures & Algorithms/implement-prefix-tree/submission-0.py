class TriNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TriNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if not c in curr.children:
                curr.children[c] = TriNode()
            curr = curr.children[c]
        curr.eow = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if not c in curr.children:
                return False
            curr = curr.children[c]
        return True
        