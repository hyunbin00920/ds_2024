from list.listNode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def insert(self, i: int, newItem) -> None:
        if i < 0 or i > self.__numItems:
            raise IndexError("Index out of bounds")
        
        newNode = ListNode(newItem, None)
        prevNode = self.getNode(i - 1)
        newNode.next = prevNode.next
        prevNode.next = newNode
        self.__numItems += 1

    def append(self, newItem) -> None:
        self.insert(self.__numItems, newItem)

    def pop(self, i: int = -1):
        if self.isEmpty():
            raise IndexError("pop from empty list")
        
        if i == -1:
            i = self.__numItems - 1
        
        if i < 0 or i >= self.__numItems:
            raise IndexError("Index out of bounds")
        
        prevNode = self.getNode(i - 1)
        item = prevNode.next.item
        prevNode.next = prevNode.next.next
        self.__numItems -= 1
        return item

    def remove(self, x):
        prevNode = self.findNode(x)
        if prevNode:
            prevNode.next = prevNode.next.next
            self.__numItems -= 1

    def get(self, i: int):
        return self.getNode(i).item

    def index(self, x):
        current = self.__tail.next
        index = 0
        while current != self.__tail:
            if current.item == x:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{x} is not in list")

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__tail.next = self.__tail
        self.__numItems = 0

    def count(self, x) -> int:
        count = 0
        current = self.__tail.next
        while current != self.__tail:
            if current.item == x:
                count += 1
            current = current.next
        return count

    def extend(self, a):
        for item in a:
            self.append(item)

    def copy(self) -> 'CircularLinkedList':
        new_list = CircularLinkedList()
        current = self.__tail.next
        while current != self.__tail:
            new_list.append(current.item)
            current = current.next
        return new_list

    def reverse(self) -> None:
        prev = None
        current = self.__tail.next
        while current != self.__tail:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__tail.next = prev

    def sort(self) -> None:
        items = [item for item in self]
        items.sort()
        self.clear()
        self.extend(items)

    def findNode(self, x):
        prevNode = self.__tail
        current = self.__tail.next
        while current != self.__tail:
            if current.item == x:
                return prevNode
            prevNode = current
            current = current.next
        return None

    def getNode(self, i: int) -> ListNode:
        if i < -1 or i >= self.__numItems:
            raise IndexError("Index out of bounds")
        
        current = self.__tail
        for _ in range(i + 1):
            current = current.next
        return current

    def printList(self) -> None:
        current = self.__tail.next
        while current != self.__tail:
            print(current.item, end=" ")
            current = current.next
        print()

    def __iter__(self):
        return CircularLinkedListIterator(self)


class CircularLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
