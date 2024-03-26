from list.listNode import *

class CircularLinkedList:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__head.next = self.__head  # ����� ���� ��带 �ڱ� �ڽ����� �����Ͽ� ��ȯ ���� ����
        self.__tail = self.__head
        self.__numItems = 0

    def insert(self, i: int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if newNode.next is self.__head:  # �� ��尡 ������ ����� ���, tail ������Ʈ
                self.__tail = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")

    def append(self, newItem) :
        newNode = ListNode(newItem, self.__head)  # �� ����� ���� ��带 ���� ����
        self.__tail.next = newNode  # ���� ������ ����� ���� ��带 �� ���� ����
        self.__tail = newNode  # tail ������Ʈ
        self.__numItems += 1

    # i��° ���� ����
    def pop(self, i: int):
        if i >= -self.__numItems and i < self.__numItems:
            i %= self.__numItems
            if i < 0:
                i += self.__numItems
            prev = self.getNode(i - 1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            if curr == self.__tail:  # ������ ��尡 ������ ����� ���, tail ������Ʈ
                self.__tail = prev
            self.__numItems -= 1
            return retItem
        else:
            return None
    
    # ���� x ����
    def remove(self, x):
        (prev, curr) = self.findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:  # ������ ��尡 ������ ����� ���, tail ������Ʈ
                self.__tail = prev
            self.__numItems -= 1
            return x
        else :
            return None
         
    # i��° ���� �˷��ֱ�
    def get(self, i:int) :
        if self.isEmpty() :
            return None
        if (i >= 0 and i <= self.__numItems - 1) :
            return self.getNode(i).item
        else:
            return None
        
    # x�� �� ��°���� �˷��ֱ�
    def index(self, x) -> int :
        curr = self.__head.next
        for index in range(self.__numItems) :
            if curr.item == x :
                return index
            else :
                curr = curr.next
        return -2
    
    # ��Ÿ �۾���
    def isEmpty(self) -> bool :
        return self.__numItems == 0
    
    def size(self) -> int :
        return self.__numItems
    
    def clear(self):
        self.__head.next = self.__head  # ����� ���� ��带 �ڱ� �ڽ����� �����Ͽ� ��ȯ ���� ����
        self.__tail = self.__head
        self.__numItems = 0

    def count(self, x) -> int :
        cnt = 0
        curr = self.__head.next
        while curr != self.__head:  # ��忡 ������ ������ ��ȸ
            if curr.item == x :
                cnt += 1
            curr = curr.next
        return cnt
    
    def extend(self, a) :
        for index in range(a.size()) :
            self.append(a.get(index))

    def copy (self) :
        a = CircularLinkedList()
        for index in range(self.__numItems) :
            a.append(self.get(index))
        return a
    
    def reverse(self) :
        a = CircularLinkedList()
        for index in range(self.__numItems) :
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()) :
            self.append(a.get(index))

    def sort(self) -> None :
        a = []
        for index in range(self.__numItems) :
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)) :
            self.append(a[index])

    def findNode(self,x) :
        prev = self.__head
        curr = prev.next
        while curr != self.__head :
            if curr.item == x :
                return (prev,curr)
            else :
                prev = curr; curr = curr.next
        return (None, None)
    
    # i�� ��� �˷��ֱ�
    def getNode(self, i:int) -> ListNode :
        curr = self.__head
        for index in range(i+1) :
            curr = curr.next
        return curr
    
    def printList(self) :
        curr = self.__head.next
        while curr != self.__head :
            print(curr.item, end = ' ')
            curr = curr.next
        print()
