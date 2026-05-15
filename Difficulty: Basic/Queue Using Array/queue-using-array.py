class myQueue:
    def __init__(self, n):
        self.capacity = n
        self.queue = [0] * n  
        self.front = 0
        self.rear = -1
        self.current_size = 0

    def isEmpty(self):
        return self.current_size == 0

    def isFull(self):
        return self.current_size == self.capacity

    def enqueue(self, x):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = x
            self.current_size += 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            self.current_size -= 1

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]