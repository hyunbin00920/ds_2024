from list.listNode import ListNode

class CircularLinkedList :
    def __init__(self) :
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def insert(self, i:int, newItem) -> None :
        if i >= 0 and i <= self.__numItems :
            prev = self.getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else :
            print("index", i, ": out of bound in insert()")

    def append(self, newItem) -> None :
        pass

    def pop(self, *args) :
        if len(args) != 0 :
            i = args[0]
        if len(args) == 0 or i == -1 :
            i = self.__numItems - 1
        if (i >= 0 and i <= self.__numItems - 1) :
            prev = self.getNode(i-1)
            retItem = prev.next.item
            prev.next = prev.next.next
            self.__numItems = -1
            return numItems
        else : 
            return None
        

    def remove(self, x) :
        pass

    def get(self, *args) :
        pass

    def index(self, x) -> int :
        pass

    def isEmpty(self) -> bool :
        pass

    def size(self) -> int :
        pass

    def clear(self) :
        pass
    
    def count(self, x) -> int :
        pass

    def extend(self, a) :
        pass

    def copy(self) -> b'CircularLinkedList' :
        pass

    def reverse(self) -> None :
        pass

    def sort(self) -> None :
        pass

    def findNode(self, x) :
        pass

    def getNode(self, i:int) -> ListNode :
        pass

    def printList(self) -> None :
        pass

    def __iter__(self) :
        return CircularLinkedListIterator(self)
    
class CircularLinkedListIterator :
    def __init__(self, alist) :
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self) :
        if self.iterPosition == self.__head :
            raise StopIteration
        else :
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item