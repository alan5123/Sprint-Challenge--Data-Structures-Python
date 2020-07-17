
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.index] = item
            if self.index < self.capacity - 1:
                self.index += 1
            else:
                self.index = 0

    def get(self):
        return self.storage