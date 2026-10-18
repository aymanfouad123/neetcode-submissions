class TrieNode:
    def __init__(self):
        # approach: using arrays
        self.children = [None]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            pos = ord(c) - ord("a")
            if curr.children[pos] == None:
                curr.children[pos] = TrieNode() 
            curr = curr.children[pos]
        # last letter
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            pos = ord(c) - ord("a")
            if curr.children[pos] == None:
                return False
            curr = curr.children[pos]
        
        # last letter
        return curr.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            pos = ord(c) - ord("a")
            if curr.children[pos] == None:
                return False
            curr = curr.children[pos]
        
        return True
        