class CacheSimulator:
	def __init__(self, cache_slots):
		self.cache_slots = cache_slots
		self.cache_hit = 0
		self.tot_cnt = 1
		self.cache = []

	def lru_sim(self, page):	   
		if (self.tot_cnt == 1) :
			self.cache.append(page)
		else :			
			if(page in self.cache) :
				self.cache_hit += 1
				self.cache.remove(page)
				self.cache.append(page)
			else :
				if (len(self.cache) + 1 > self.cache_slots) :
					self.cache.pop(0)
					self.cache.append(page)
				else :
					self.cache.append(page)
		self.tot_cnt += 1

	def print_stats(self):
		hit_ratio = self.cache_hit / self.tot_cnt
		print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = {}".format(hit_ratio))

if __name__ == "__main__":
	data_file = open("./linkbench.trc")
	lines = data_file.readlines()
	for cache_slots in range(100, 1001, 100):
		cache_sim = CacheSimulator(cache_slots)
		for line in lines:
			page = line.split()[0]
			cache_sim.lru_sim(page)
		
		cache_sim.print_stats()
