from Queue.listQueue import *

class DoubleQueue :
    def __init__(self) :
        self.__q = ListQueue()
        self.__tq = ListQueue()

    def move_elts(self,q,tq) :
        while not self.__q.isEmpty() :
            self.__q.enqueue(self.__tq.dequeue())
    
    def push(self, x) :
        self.move_elts(self.__q,self.__tq)
        self.__tq.enqueue(x)
        self.move_elts(self.__q,self.__tq)

    def pop(self, x) :
        return self.__q.dequeue()
