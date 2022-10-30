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

class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def get_nearest_prime(self, start, stop, step=1):
		start = self.size
		lst = [2, 3, 5]
		for i in range(start, stop, step):
			for j in lst:
				if i % j == 0:
					break
			else:
				lst.append(i)
		return lst[-1]

	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = UnorderedList()
			self.data[hashvalue] = UnorderedList()
			self.slots[hashvalue].append(key)
			self.data[hashvalue].append(data)
		else:
			if self.slots[hashvalue].search(key):
				idx = self.slots[hashvalue].index(key)
				self.data[hashvalue].pop(idx)
				self.data[hashvalue].insert(idx, data)
			else:
				self.slots[hashvalue].append(key)
				self.data[hashvalue].append(data)

		if (self.__len__()/self.size > 0.7):
			last_size = self.size
			self.size = self.get_nearest_prime(self.size, 2*self.size)
			self.slots += [None] * (self.size - last_size)
			self.data += [None] * (self.size - last_size)

	def hashfunction(self, key, size):
		if isinstance(key, str):
			key = len(key)
		return key % size

	def rehash(self, oldhash, size):
		return (oldhash + 1) % size

	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while not found and not stop:
			if self.slots[position] != None:
				if self.slots[position].search(key):
					found = True
					idx = self.slots[position].index(key)
					data = self.data[position].pop(idx)
					self.data[position].insert(idx, data)
			
			position = self.rehash(position, len(self.slots))	
			if position == startslot:
				stop = True
					
		if (self.__len__()/self.size > 0.7):
			last_size = self.size
			self.size = self.get_nearest_prime(self.size, 2*self.size)
			self.slots += [None] * (self.size - last_size)
			self.data += [None] * (self.size - last_size)
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)

	def __len__(self):
		count = 0
		for i in range(self.size):
			if self.slots[i] != None:
				count += 1
		return count

	def __contains__(self, item):
		found = False
		for i in range(self.size):
			if self.data[i] != None and self.data[i].search(item):
				found = True
				break
		return found
	
	def __delitem__(self, key):
		idxList = -1
		idxItem = -1
		for i in range(self.size):
			if self.slots[i] != None and self.slots[i].search(key):
				idxList = i
				idxItem = self.slots[i].index(key)
				break
		if idxItem >= 0:
			self.slots[idxList].pop(idxItem)
			self.data[idxList].pop(idxItem)
			if self.slots[idxList].size() == 0:
				self.slots[idxList] = None
				self.data[idxList] = None
		
		if self.__len__()/self.size < 0.2:
			slots = []
			data = []
			for i in range(self.size):
				if self.slots[i] != None:
					for _ in range(self.slots[i].size()):
						slots.append(self.slots[i].pop())
						data.append(self.data[i].pop())
			self.size = self.get_nearest_prime(self.size, self.size//2, -1)
			self.slots = [None] * self.size
			self.data = [None] * self.size
			for i in range(len(slots)):
			  self.put(slots[i], data[i])

H = HashTable()
mystr = input().split()
for word in mystr:
	if H[word] == None:
		H[word] = 1
	else:
		H[word] += 1
	print(H[word])
