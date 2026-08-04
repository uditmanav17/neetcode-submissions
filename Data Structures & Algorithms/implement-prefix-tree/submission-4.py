class PrefixTree:

    def __init__(self):
        self.root = {}
        self.end = ""
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node.setdefault(char, {})
            node = node.get(char)
        node[self.end] = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            node = node.get(char, None)
            if not node:
                return False
        return self.end in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            node = node.get(char, None)
            if not node:
                return False
        return True

