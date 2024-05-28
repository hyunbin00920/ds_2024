from Heap.heap_node import *

class CacheSimulator :
  def __init__ (self, cache_slots) :
    self.cache_slots = cache_slots
    self.cache_hit = 0
    self.tot_cnt = 0
    self.cache = Heap_node()              # Heap for Cache
    self.freq_dic = {}                    # Dictionary for storing frequency on lpn

  def lfu_sim (self, lpn) :
    
  # Check the Existency of the data in cache
    i = self.cache.getindex(lpn)

  # The data is in cache
    if i != -1 :
      self.cache_hit += 1
      self.freq_dic[lpn] += 1
      self.cache.UpdateNode(i)
            
  # The data is not in cache
    else :

    # Cache is full
      if self.cache_slots == self.cache.size() :
        self.cache.deleteMin()

      # The data has been Updated before
        if lpn in self.freq_dic :
          self.freq_dic[lpn] += 1
          
      # The data has not been Updated before
        else :
          self.freq_dic[lpn] = 1

    # Cache is not full (then it must not been Updated before)
      else :
        self.freq_dic[lpn] = 1

      self.cache.insert(Node(lpn,self.freq_dic[lpn]))
    
    self.tot_cnt += 1

  def print_stats(self) :
    hit_ratio = self.cache_hit / self.tot_cnt
    print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = {}".format(hit_ratio))

if __name__ == "__main__":
  data_file = open("./linkbench.trc")
  lines = data_file.readlines()
  for cache_slots in range(100, 1001, 100):
    cache_sim = CacheSimulator(cache_slots)
    for line in lines :
      lpn = line.split()[0]
      cache_sim.lfu_sim(lpn)

    cache_sim.print_stats()
