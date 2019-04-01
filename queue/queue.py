class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.insert(0, item)

    def dequeue(self):
        if self.len() == 0:
            return None
        return self.storage.pop(len(self.storage) - 1)

    def len(self):
        return len(self.storage)
