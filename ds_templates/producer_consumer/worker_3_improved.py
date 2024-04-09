from listQueue import ListQueue
import threading
import time

class Producer:
	def __init__(self, items, pr, Queue_normal, Queue_gold, Queue_platinum):
		self.__alive = True

		self.items = items
		self.priorities = pr
		
		self.worker = threading.Thread(target = self.run)
		
		self.ProducerQueue_normal = Queue_normal
		self.ProducerQueue_gold = Queue_gold
		self.ProducerQueue_platinum = Queue_platinum

	def get_item(self):
		while not self.items.isEmpty() :
			item = self.items.dequeue()
			priority = self.priorities.dequeue()
			return item,priority

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
	def __init__(self, Queue_normal, Queue_gold, Queue_platinum):
		self.__alive = True

		self.ConsumerQueue_normal = Queue_normal
		self.ConsumerQueue_gold = Queue_gold
		self.ConsumerQueue_platinum = Queue_platinum

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
	priority = ListQueue()
	names = ListQueue()

	for c in customers:
		priority.enqueue(c[0])
		names.enqueue(c[1])

	Queue_normal = ListQueue()
	Queue_gold = ListQueue()
	Queue_platinum = ListQueue()

	producer = Producer(names, priority, Queue_normal, Queue_gold, Queue_platinum)

	consumer = Consumer(Queue_normal, Queue_gold, Queue_platinum)  

	producer.start()
	consumer.start()

	time.sleep(1.5)
		
	producer.finish()
	consumer.finish()