class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        # max size of the queue
        self.k = k
        # list
        self.queue = [None] * k
        self.head = 0
        self.tail = 0
        self.full = False
        self.empty = True

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # if queue is full just return false else return true
        if self.isFull():
            return False

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        if self.head == self.tail:
            self.full = True
        else:
            self.full = False
        self.empty = False
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        # remove last element and increase head
        self.head = (self.head + 1) % self.k
        if self.head == self.tail:
            self.empty = True
        else:
            self.empty = False
        self.full = False
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.k]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.empty

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.full
