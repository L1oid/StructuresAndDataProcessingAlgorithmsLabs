import sys


class MaxHeap:
    def __init__(self):
        self._heapList = [sys.maxsize]
        self.currentSize = 0

    @property
    def heapList(self):
        return self._heapList[1:]

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if (self.currentSize // 2) <= pos <= self.currentSize:
            return True
        return False

    def swap(self, fpos, spos):
        self._heapList[fpos], self._heapList[spos] = self._heapList[spos], self._heapList[fpos]

    def maxHeapify(self, pos):
        if not self.isLeaf(pos):
            if self._heapList[pos] < self._heapList[self.leftChild(pos)] or \
                    self._heapList[pos] < self._heapList[self.rightChild(pos)]:
                if self._heapList[self.leftChild(pos)] > self._heapList[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    def insert(self, element):
        self.currentSize += 1
        self._heapList.append(element)

        current = self.currentSize

        while self._heapList[current] > self._heapList[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def buildHeap(self, alist):
        for value in alist:
            self.insert(value)


bh = MaxHeap()
bh.buildHeap([9, 5, 6, 2, 3])

print(bh.heapList)
