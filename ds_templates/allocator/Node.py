class FreeListNode:
    def __init__(self, base:int, bound:int, prevNode:'FreeListNode', nextNode:'FreeListNode'):
        self.base = base
        self.bound = bound
        self.prev = prevNode
        self.next = nextNode


