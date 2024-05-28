from Node import FreeListNode

class FreeList_firstfit :
    def __init__(self) :
        self.__head = FreeListNode(0, 0, None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def getNode(self, i:int) -> FreeListNode :
        curr = self.__head
        for index in range(i + 1) :
            curr = curr.next
        return curr

    # Insert new FreeListNode at index i
    def insert(self, i:int, newbase, newbound) -> None :
        if (i >= 0 and i <= self.__numItems) :
            prev = self.getNode(i - 1)
            newNode = FreeListNode(newbase, newbound, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else :
            print("index", i, ": out of bound in insert()")

    # Append new FreeListNode at last of list
    def append(self, newbase, newbound) -> None :
        prev = self.__head.prev
        newNode = FreeListNode(newbase, newbound, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1

    # Change node's info with index
    def change_info(self, i:int, base_diff:int, bound_diff:int) :
        if i == -1 :
            i = self.__numItems - 1

        curr = self.getNode(i)

        curr.base += base_diff
        curr.bound += bound_diff

        if curr.bound == 0 :
            self.remove(curr)

    # Finding index for Node with base 
    def find_index(self, base) : 
        index = 1
        curr = self.getNode(index)
        while (curr != self.__head and curr.base < base) :
            curr = curr.next
            index += 1    
        return index
    
    # Verify Merging the Node is possible with previous or next Node And Merge
    def merge(self, index) -> FreeListNode:
        currNode = self.getNode(index)
        prevNode = currNode.prev; nextNode = currNode.next
        # If the Node can Merge with previous Node
        if (prevNode.base + prevNode.bound == currNode.base and prevNode != self.__head):
            currNode.base = prevNode.base
            currNode.bound += prevNode.bound
            prevNode.prev.next = currNode
            currNode.prev = prevNode.prev
            self.__numItems -= 1

        # If the Node can Merge with next Node
        if currNode.base + currNode.bound == nextNode.base :
            currNode.bound += nextNode.bound
            currNode.next = nextNode.next
            nextNode.next.prev = currNode
            self.__numItems -= 1

        return currNode
    
    # Remove Node
    def remove(self, curr:FreeListNode) :
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.__numItems -= 1

    # Chunk_deallocation
    def chunk_deallocation(self, Node:FreeListNode, csize, ccnt) :
        for i in range(1, ccnt) :
            tbase = csize*i; tnextbase = csize*(i+1)    # temp chunk unit
            if Node.base <= tbase and Node.base + Node.bound >= tnextbase :     # If temp chunk can allocated at the Node
                if Node.bound == csize :                                            # If FreeNode has exactly chunk size bound
                    self.remove(Node)
                else :                                                              # If not
                    Node.bound -= csize
                    Node = Node.next
                    while Node != self.__head :                                 # Changing info behind the Node
                        Node.base -= csize; Node.bound -= csize
                        Node = Node.next
                    break
            else :
                continue 

    def print_list(self) :
        curr = self.__head.next
        while curr != self.__head :
            print("(", curr.base, ",", curr.bound, ")")
            curr = curr.next

    def print_list_to_file(self, file) :
        curr = self.__head.next
        while curr != self.__head:
            file.write(f"({curr.base}, {curr.bound})\n")
            curr = curr.next

    def __iter__(self) :
        return FreeListIterator(self)
    
class FreeListIterator :
    def __init__(self, alist) :
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self) :
        if self.iterPosition == self.__head :
            raise StopIteration
        else :
            rtnval = (self.iterPosition.base, self.iterPosition.bound)
            self.iterPosition = self.iterPosition.next
            return rtnval

    
