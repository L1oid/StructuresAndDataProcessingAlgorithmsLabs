class BinHeap:
    def __init__(self, siz):
        self.heapList = [0]
        self.currentSize = 0
        self.siz = siz

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        if self.currentSize + 1 > self.siz:
            self.delMin()
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        for v in alist:
            self.insert(v)

        i = self.currentSize // 2
        while (i > 0):
            self.percDown(i)
            i = i - 1


bh = BinHeap(3)
bh.buildHeap([9, 5, 6, 2, 3])
print(bh.heapList)

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
