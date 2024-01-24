class Node:
    def __init__(self):
        self.val = 0
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def get(self, index: int) -> int:
        print(index,self.length)
        current_node = self.head
        count = -1
        while current_node.next != None :
            current_node = current_node.next
            count+=1
            if count == index:
                return current_node.val
        print(count)
        return -1



    def addAtHead(self, val: int) -> None:
        if self.head == self.tail:
            self.addAtTail(val)
        else:
            newNode = Node()
            newNode.val = val
            newNode.next = self.head.next
            self.head.next = newNode
            self.length += 1



    def addAtTail(self, val: int) -> None:
        newNode = Node()
        newNode.next = None
        newNode.val = val
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            newNode = Node()
            newNode.val = val
            current_node = self.head
            count = -1
            while current_node != None:
                if count+1 == index:
                    newNode.next = current_node.next
                    current_node.next = newNode
                    self.length += 1
                    return
                current_node = current_node.next
                count += 1



    def deleteAtIndex(self, index: int) -> None:
        current_node = self.head
        count = -1
        while current_node != None:
            if count + 1 == index and current_node.next != None:
                self.length -= 1
                current_node.next = current_node.next.next
                if count + 1 == self.length:
                    current_node.next = None
                    self.tail = current_node
            current_node = current_node.next
            count +=1

    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)