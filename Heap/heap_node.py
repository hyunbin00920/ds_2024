from Heap.lpn_node import *

class Heap_node :
	def __init__(self, *args) :
		if len(args) != 0 :
			self.array = args[0]
		else :
			self.array = []

	def insert(self, x) :
		self.array.append(x)
		self.__percolateUp(len(self.array) - 1)

	def __percolateUp(self, i:int) :
		parent = (i - 1) // 2
		if i > 0 and self.array[i].freq < self.array[parent].freq :
			self.array[i], self.array[parent] = self.array[parent], self.array[i]
			self.__percolateUp(parent)

	def deleteMin(self) :
		if (not self.isEmpty()) :
			max = self.array[0]
			self.array[0] = self.array.pop()
			self.__percolateDown(0)
			return max
		else :
			return None
		
	def __percolateDown(self, i:int) :
		child = 2 * i + 1
		right = 2 * i + 2
		if (child <= len(self.array) - 1 ) :
			if (right <= len(self.array) - 1 and self.array[child].freq > self.array[right].freq) :
				child = right
			if self.array[i].freq > self.array[child].freq :
				self.array[i], self.array[child] = self.array[child], self.array[i]
				self.__percolateDown(child)
		
	def max(self) :
		return self.array[0]
			
	def buildHeap(self) :
		for i in range((len(self.array) - 2) // 2, -1, -1) :
			self.__percolateDown(i)

	def isEmpty(self) -> bool :
		return len(self.array) == 0
			
	def clear(self) :
		self.array = []

	def size(self) -> int :
		return len(self.array)
	
	# If data is in Heap, return index of the data
	# If not, return -1
	def getindex(self, x) :				
		i = 0		
		for node in self.array :
			if node.lpn == x :
				return i				
			else :
				i += 1
		return -1
	
	# Increase frequency of data at index i
	# And percloateDown from i
	def UpdateNode(self, i:int) :
		self.array[i].freq += 1
		self.__percolateDown(i)