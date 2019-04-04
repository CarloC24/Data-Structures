class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        n = len(self.storage) - 1
        for node in range(n//2, -1, -1):
            self._sift_down(node)
        return

    def delete(self):
        n = len(self.storage)
        self.swap(0, n)
        max = self.storage.pop(0)
        self._bubble_up(n - 2)   # furthest left node
        return max

    def get_max(self):
        maxVal = 0
        for i in self.storage:
            if i > maxVal:
                maxVal = i
        return maxVal

    def get_size(self):
        # length = len(self.storage)
        # return length
        pass

    def _bubble_up(self, index):
        parent = (index - 1)//2
        if self.storage[parent] < self.storage[index]:
            self.swap(index, parent)
    # base case; we've reached the top of the heap
        if parent <= 0:
            return
        else:
            self.bubble_up(parent)

    def _sift_down(self, index):
        child = 2 * index + 1
        # base case, stop recursing when we hit the end of the heap
        if child > len(self.storage) - 1:
            return
        # check that second child exists; if so find max
        if (child + 1 <= len(self.storage) - 1) and (self.storage[child+1] > self.storage[child]):
            child += 1
        # preserves heap structure
        if self.storage[index] < self.storage[child]:
            self.swap(index, child)
            self._sift_down(child)
        else:
            return

    def swap(self, index, child):
        self.storage[index], self.storage[child] = self.storage[child], self.storage[index]
        return
