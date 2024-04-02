from listQueue import ListQueue
import threading
import time

class Producer:
    def __init__(self, items, pr):
        self.__alive = True

        self.items = items
        self.priorities = pr
        
        self.pos = 0
        self.worker = threading.Thread(target = self.run)
        
        self.ProducerQueue_normal = ListQueue()
        self.ProducerQueue_gold = ListQueue()
        self.ProducerQueue_platinum = ListQueue()

    def get_item(self):
        if self.pos < len(self.items) :
            item = self.items[self.pos]
            priority = self.priorities[self.pos]
            self.pos += 1
            return item,priority
        else :
            return None

    def run(self):
        while True :
            time.sleep(0.01)
            if self.__alive :
                item = self.get_item()
                if (item != None) :
                    print("Arrived :",item[0])
                    if (item[1] == '1') :
                        self.ProducerQueue_normal.enqueue(item[0])
                    elif (item[1] == '2') :
                        self.ProducerQueue_gold.enqueue(item[0])
                    elif (item[1] == '3') :
                        self.ProducerQueue_platinum.enqueue(item[0])
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
    def __init__(self,items1, items2, items3):
        self.__alive = True
        self.ConsumerQueue_normal = items1
        self.ConsumerQueue_gold = items2
        self.ConsumerQueue_platinum = items3
        self.worker = threading.Thread(target = self.run)

    def run(self):
        while True :
            time.sleep(0.05)
            if self.__alive :
                if (self.ConsumerQueue_platinum.isEmpty()) :
                    if (self.ConsumerQueue_gold.isEmpty()) :
                        if (self.ConsumerQueue_normal.isEmpty()) :
                            pass
                        else :
                            print("Boarding :", self.ConsumerQueue_normal.dequeue())
                    else :
                        print("Boarding :", self.ConsumerQueue_gold.dequeue())
                else :
                    print("Boarding :", self.ConsumerQueue_platinum.dequeue())

                
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


    # Priority 
    priority = []
    names = []

    for c in customers:
        priority.append(c[0])
        names.append(c[1])

    producer = Producer(names, priority)

    consumer = Consumer(producer.ProducerQueue_normal, producer.ProducerQueue_gold, producer.ProducerQueue_platinum)  

    producer.start()
    consumer.start()
    time.sleep(1.5)
    producer.finish()
    consumer.finish()
