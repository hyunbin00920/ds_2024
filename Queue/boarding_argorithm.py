from Queue.listQueue import *

def makeQueue(cnt) :
    q = ListQueue()
    cnt += 1
    return q

def main() :
    cnt = 0

    q = makeQueue(cnt)
    tq = makeQueue(cnt)
    ttq = makeQueue(cnt)

    print(cnt)

    q.enqueue(1)

    tq.enqueue(2)
    tq.enqueue(4)

    ttq.enqueue(3)
    ttq.enqueue(5)

    q.printQueue()
    tq.printQueue()
    ttq.printQueue()

if __name__ == "__main__" :
    main()
