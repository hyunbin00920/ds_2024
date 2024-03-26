from list.listNode import *

class CircularLinkedList:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__head.next = self.__head  # 헤드의 다음 노드를 자기 자신으로 설정하여 순환 구조 만듦
        self.__tail = self.__head
        self.__numItems = 0

    def insert(self, i: int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if newNode.next is self.__head:  # 새 노드가 마지막 노드인 경우, tail 업데이트
                self.__tail = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")

    def append(self, newItem) :
        newNode = ListNode(newItem, self.__head)  # 새 노드의 다음 노드를 헤드로 설정
        self.__tail.next = newNode  # 이전 마지막 노드의 다음 노드를 새 노드로 설정
        self.__tail = newNode  # tail 업데이트
        self.__numItems += 1

    # i번째 원소 삭제
    def pop(self, i: int):
        if i >= -self.__numItems and i < self.__numItems:
            i %= self.__numItems
            if i < 0:
                i += self.__numItems
            prev = self.getNode(i - 1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            if curr == self.__tail:  # 삭제된 노드가 마지막 노드인 경우, tail 업데이트
                self.__tail = prev
            self.__numItems -= 1
            return retItem
        else:
            return None
    
    # 원소 x 삭제
    def remove(self, x):
        (prev, curr) = self.findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:  # 삭제된 노드가 마지막 노드인 경우, tail 업데이트
                self.__tail = prev
            self.__numItems -= 1
            return x
        else :
            return None
         
    # i번째 원소 알려주기
    def get(self, i:int) :
        if self.isEmpty() :
            return None
        if (i >= 0 and i <= self.__numItems - 1) :
            return self.getNode(i).item
        else:
            return None
        
    # x가 몇 번째인지 알려주기
    def index(self, x) -> int :
        curr = self.__head.next
        for index in range(self.__numItems) :
            if curr.item == x :
                return index
            else :
                curr = curr.next
        return -2
    
    # 기타 작업들
    def isEmpty(self) -> bool :
        return self.__numItems == 0
    
    def size(self) -> int :
        return self.__numItems
    
    def clear(self):
        self.__head.next = self.__head  # 헤드의 다음 노드를 자기 자신으로 설정하여 순환 구조 만듦
        self.__tail = self.__head
        self.__numItems = 0

    def count(self, x) -> int :
        cnt = 0
        curr = self.__head.next
        while curr != self.__head:  # 헤드에 도달할 때까지 순회
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
    
    # i번 노드 알려주기
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
