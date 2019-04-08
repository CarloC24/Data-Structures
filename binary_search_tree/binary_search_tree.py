class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if self.value > value:
                if self.left == None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif self.value < value:
                if self.right == None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def contains(self, target):
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                if self.left is None:
                    return False
                return self.left.contains(target)
        else:
            return True

    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
