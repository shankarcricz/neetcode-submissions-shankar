class Trie:
    def __init__(self, val=None):
        self.val = val
        self.isEnd = False
        self.arr = [0 for i in range(26)]
        

class PrefixTree:

    def __init__(self):
        self.root = Trie()
        

    def insert(self, word: str) -> None:
        trie = self.root
        for w in word:
            if trie.arr[ord(w) -ord('a')]:
                trie = trie.arr[ord(w) -ord('a')]

            else:
                trie.arr[ord(w) -ord('a')] =  Trie(w)
                trie = trie.arr[ord(w) -ord('a')]
        trie.isEnd = True
        



    def search(self, word: str) -> bool:
        trie = self.root
        for w in word:
            if trie.arr[ord(w) -ord('a')]:
                trie = trie.arr[ord(w) -ord('a')]
        if trie.isEnd: return True
        return False

        

    def startsWith(self, prefix: str) -> bool:
        trie = self.root
        for w in prefix:
            if trie.arr[ord(w) -ord('a')]:
                trie = trie.arr[ord(w) -ord('a')]
            else:
                return False
        return True

        
        