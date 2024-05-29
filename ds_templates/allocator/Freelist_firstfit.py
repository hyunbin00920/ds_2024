from Node import FreeListNode

class FreeList_firstfit :
    # Circular Doubly Linked List
    def __init__(self) :
        self.head = FreeListNode(0, 0, None, None)
        self.head.prev = self.head
        self.head.next = self.head
        self.__numItems = 0

    # Get Node with index
    def getNode(self, i:int) -> FreeListNode :
        if i == -1 :
            i = self.__numItems - 1
        curr = self.head.next
        for index in range(i) :
            curr = curr.next
        # print(f"GETNODE {i}: ({curr.base}, {curr.bound})")
        return curr

    # Insert new FreeListNode at index i
    def insert(self, i:int, newbase, newbound) -> None :
        if (i >= 0 and i <= self.__numItems) :
            if i == 0 :
                prev = self.head
            else :
                prev = self.getNode(i-1)
            newNode = FreeListNode(newbase, newbound, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else :
            print("index", i, ": out of bound in insert()")

    # Append new FreeListNode at last of list
    def append(self, newbase, newbound) -> None :
        prev = self.head.prev
        newNode = FreeListNode(newbase, newbound, prev, self.head)
        prev.next = newNode
        self.head.prev = newNode
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
        index = 0
        curr = self.getNode(index)
        while (curr != self.head and curr.base <= base) :
            curr = curr.next
            index += 1    
        return index
    
    # Verify Merging the Node is possible with previous or next Node And Merge
    def merge(self, index) -> FreeListNode:
        currNode = self.getNode(index)
        prevNode = currNode.prev; nextNode = currNode.next
        # If the Node can Merge with previous Node
        if (prevNode.base + prevNode.bound == currNode.base and prevNode != self.head):
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

    # Chunk allocation
    def chunk_allocation(self, csize, ccnt) :
        temp = self.getNode(-1) 
        if ((temp.base + temp.bound) % csize) == 0 :
            self.change_info(-1, 0, csize)
        else :
            self.append(csize * (ccnt-1), csize)

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
                    while Node != self.head :                                 # Changing info behind the Node
                        Node.base -= csize; Node.bound -= csize
                        Node = Node.next
                    break
            else :
                continue 

    # (ETC) Debugging function
    def print_list(self) :
        print(" PRINT LIST ")
        curr = self.head.next
        index = 0
        while curr != self.head :
            print(f"index {index} = ({curr.base}, {curr.bound})")
            index += 1
            curr = curr.next
            
    def print_list_to_file(self, file) :
        curr = self.head.next
        while curr != self.head:
            file.write(f"({curr.base}, {curr.bound})\n")
            curr = curr.next


    
