class LRUCounter:
    def __init__(self):
        self.counter = {}

    def hit(self, key):
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 1

    def most_used(self):
        if not self.counter:
            return None

        return max(self.counter, key=self.counter.get)

LRU = LRUCounter()
LRU.hit("a")
LRU.hit("a")
LRU.hit("b")
LRU.hit("b")
LRU.hit("b")
LRU.hit("c")
LRU.hit("c")
LRU.hit("c")
LRU.hit("c")

print(LRU.most_used())