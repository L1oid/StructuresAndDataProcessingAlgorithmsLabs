class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        output = "["
        while current != None:
            output += str(current.getData()) + ", "
            current = current.getNext()
        output = output[:-2] + "]"
        return output

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        if current == None:
            self.add(item)
            return
        while current.getNext() != None:
            current = current.getNext()
        temp = Node(item)
        temp.setNext(None)
        current.setNext(temp)

    def index(self, item):
        current = self.head
        index = 0
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                index += 1
                current = current.getNext()
        if not found:
            index = None
        return index

    def insert(self, pos, item):
        if self.size() < pos or pos < 0:
            return
        if pos == 0:
            self.add(item)
            return
        elif pos == self.size():
            self.append(item)
            return
        current = self.head
        for _ in range(pos-1):
            current = current.getNext()
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)

    def pop(self, pos=None):
        if self.isEmpty():
            return
        current = self.head
        if pos == None:
            while current.getNext() != None:
                current = current.getNext()
        else:
            if self.size() - 1 < pos or pos < 0:
                return
            for _ in range(pos):
                current = current.getNext()
        self.remove(current.getData())
        return current.getData()

    def slice(self, start, stop):
        if start < 0 or stop < 0 or start > self.size() or stop > self.size():
            return
        current = self.head
        copy = UnorderedList()
        for _ in range(start):
            current = current.getNext()
        for _ in range(start, stop):
            copy.append(current.getData())
            current = current.getNext()
        if copy.size() == 1:
            return copy.head.data
        return copy

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.slice(item.start, item.stop)


class Stack:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.items.size() - 1:self.items.size()]

    def size(self):
        return self.items.size()

    def __str__(self):
        current = self.items.head
        output = "["
        while current != None:
            output += str(current.getData()) + ", "
            current = current.getNext()
        output = output[:-2] + "]"
        return output

class Queue:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return self.items.size()

    def __str__(self):
        current = self.items.head
        output = "["
        while current != None:
            output += str(current.getData()) + ", "
            current = current.getNext()
        output = output[:-2] + "]"
        return output

class Deque:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.size()

    def __str__(self):
        current = self.items.head
        output = "["
        while current != None:
            output += str(current.getData()) + ", "
            current = current.getNext()
        output = output[:-2] + "]"
        return output

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.add(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

print("Stack")
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
stack.pop()
print(stack.peek())
print(stack)

print("")
print("Queue")
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
queue.dequeue()
print(queue)

print("")
print("Deque")
deque = Deque()
deque.addRear(1)
deque.addFront(2)
deque.addFront(3)
deque.addRear(4)
print(deque)
print(deque.removeFront())
print(deque)
print(deque.removeRear())
print(deque)