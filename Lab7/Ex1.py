class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['&', '|', '!', ')']:
            currentTree.setRootVal(bool(int(i)))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['&', '|']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == '!':
            parent = pStack.pop()
            currentTree = parent
            currentTree.setRootVal(i)
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return eTree


def evaluate(parseTree):
    opers = {
        '&': lambda x, y: x and y,
        '|': lambda x, y: x or y,
        '!': lambda x: not x
    }

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    elif parseTree.getRootVal() == '!':
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC))
    else:
        return parseTree.getRootVal()


def printexpr(parseTree):
    str_ = ''

    val = parseTree.getRootVal()
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        str_ += '( ' + printexpr(leftC) + ' ' + val + ' ' + printexpr(rightC) + ' )'
    else:
        if val == '!':
            str_ += '( ! ' + printexpr(leftC) + ' )'
        else:
            str_ += str(int(val))

    return str_


pt = buildParseTree("( ( ! ( 0 | 0 ) ) & ( 1 | 0 ) )")
print("evaluate:", evaluate(pt))
print('printexpr: ' + printexpr(pt))
