from collections import deque

class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.end = "*"
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            node.setdefault(char, {})
            node = node.get(char)
        node[self.end] = True
        

    def search(self, word: str) -> bool:
        node = self.trie
        candidates = deque([node])
        # print(node)
        # print(candidates)
        for char in word:
            N = len(candidates)
            for _ in range(N):
                node = candidates.popleft()
                
                if char == '.':
                    for child in node.values():
                        if isinstance(child, dict):
                            candidates.append(child)
                else:
                    if char in node:
                        candidates.append(node[char])
        return any(self.end in cand for cand in candidates)


        
