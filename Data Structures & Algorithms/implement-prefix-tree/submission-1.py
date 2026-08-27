class PrefixTree:

    def __init__(self):
        self.prefs = {}
        self.words = set()


    def insert(self, word: str) -> None:
        self.words.add(word)
        while word:
            wordlen = len(word)
            if wordlen in self.prefs:
                self.prefs[wordlen].add(word)
            else:
                self.prefs[wordlen] = set([word])
            word = word[:-1]


    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        wordlen = len(prefix)
        if prefix in self.prefs.get(wordlen, {}):
            return True
        return False
        
        