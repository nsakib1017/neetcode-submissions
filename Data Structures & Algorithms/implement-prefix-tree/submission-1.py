class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in (range(len(word))):
            if not word[i] in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in (range(len(word))):
            if not word[i] in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in (range(len(prefix))):
            if not prefix[i] in curr.children:
                return False
            curr = curr.children[prefix[i]]
        return True
        
        