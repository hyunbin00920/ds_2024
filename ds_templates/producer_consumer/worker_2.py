from listQueue import ListQueue
import threading
import time

class Producer:
    def __init__(self, items):
        self.__alive = True
        self.items = items
        self.pos = 0
        self.worker = threading.Thread(target = self.run)
        self.ProducerQueue = ListQueue()

    def get_item(self):
        if self.pos < len(self.items) :
            item = self.items[self.pos]
            self.pos += 1
            return item
        else :
            return None

    def run(self):
        while True :
            time.sleep(0.01)
            if self.__alive :
                item = self.get_item()
                if item != None :
                    print("Arrived :",item)
                    self.ProducerQueue.enqueue(item)
                else :
                    pass
            else :
                break
        
        print("Producer is dying...")

    def start(self):
        self.worker.start()

    def finish(self):
        self.__alive = False
        self.worker.join()

class Consumer:
    def __init__(self,items):
        self.__alive = True
        self.ConsumerQueue = items
        self.worker = threading.Thread(target = self.run)

    def run(self):
        while True :
            time.sleep(0.05)
            if self.__alive :
                print("Boarding :",self.ConsumerQueue.dequeue())
            else :
                break

        print("Consumer is dying...")
        
    def start(self):
        self.worker.start()
        
    def finish(self):
        self.__alive = False
        self.worker.join()
        

if __name__ == "__main__":
    
    customers = []
    with open("customer.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            customer = line.split()
            customers.append(customer)

    # FIFO
    names1 = []

    for c in customers:
        names1.append(c[1])

    producer = Producer(names1)

    consumer = Consumer(producer.ProducerQueue)    
    producer.start()
    consumer.start()
    time.sleep(1.5)
    producer.finish()
    consumer.finish()
