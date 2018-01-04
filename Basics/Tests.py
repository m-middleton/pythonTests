class Node:
    def __init__(self, data, node = None):
        self.data = data
        self.nextNode = node

    def getNext(self):
        return self.nextNode

    def setNext(self, node):
        self.nextNode  = node

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
#End Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, data, index = 0):
        if (index > self.size) | (index < 0):
            print("invalid index")
        else:
            newNode = Node(data)

            if self.size == 0:
                self.head = newNode
            elif index == 0:
                newNode.setNext(self.head)
                self.head = newNode
            else:
                current = self.head
                for i in range(1,index):
                    current = current.getNext()

                if index == self.size:
                    current.setNext(newNode)
                else:
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
            self.size += 1

    def removeIndex(self, index = 0):
        if (index > self.size) | (index < 0):
            print("invalid index")
            return false
        else:
            if index == 0:
                self.head = self.head.getNext()
            else:
                previous = self.head
                for i in range(1, index):
                    previous = previous.getNext()
                if index == self.size:
                    previous.setNext(None)
                else:
                    previous.setNext(previous.getNext().getNext())
            self.size -= 1
            return true

    def removeData(self, data):
        current = self.head
        previous = None

        while current:
            if current.getData() == data:
                if previous:
                    previous.setNext(current.getNext())
                else:
                    self.head = current.getNext()
                self.size -= 1
                self.removeData(data)   #Recursion until all indexes with inputted data are removed
                return True
            else:
                previous = current
                current = current.getNext()
        return False

    def printList(self):
        current = self.head
        print(current.getData())
        for i in range(1, self.size):
            current = current.getNext()
            print(current.getData())
#End linkedList

def testBench():
    newList = LinkedList()
    newList.addNode(3)
    newList.addNode(6)
    newList.addNode(6)
    newList.addNode(5)

    newList.addNode(10, 10)

    print('\nList: ')
    newList.printList()
    print('')

    removedVar = 6
    removed = newList.removeData(removedVar)
    print(removedVar, 'was removed:', removed)
    print('\nNewList: ')

    newList.printList()

testBench()
