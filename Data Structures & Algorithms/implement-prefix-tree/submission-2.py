class Node:
    def __init__(self):
        self.children = [None]*26
        self.has_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if (node.children[idx] == None):
                node.children[idx] = Node()
            node = node.children[idx]
        node.has_word = True

    def search(self, word: str) -> bool:
        node = self._traversal(word)
        if (node is None):
            return False
        return node.has_word

    def startsWith(self, prefix: str) -> bool:
        node = self._traversal(prefix)
        return node != None
    
    def _traversal(self, word: str) -> Node:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            node = node.children[idx]
            if (node == None):
                return None
        return node
        