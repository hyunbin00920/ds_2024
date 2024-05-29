from Node import *
from Freelist_firstfit import *
import time

class Allocator:
    def __init__(self):
        self.chunk_size = 16384                                                 # fixed value
        self.chunk_cnt = 1

        self.used_size = 0                                                      # Set default Used size
        self.free_size = 16384                                                  # Set default Free size

        self.freelist = FreeList_firstfit()                                     # Circular Doubly Linked List
        self.freelist.append(0,16384)                                           # Set default Free Node

        self.object_dic = {}                                                    # Dictionary For allocated object's informations(base, bound)
        
        
    def print_stats(self):
        self.Arena_size = self.used_size + self.free_size
        self.Utilization = float(self.used_size) / float(self.Arena_size)
        # print(f"Chunk Count : {self.chunk_cnt}")
        print("Arena  :", self.chunk_size * self.chunk_cnt, "B")
        print("In-use :", self.used_size, "B")
        print("Free   :", self.free_size, "B")
        print(f"Utilization: {self.Utilization * 100:5f} %")


    def malloc(self, id, size):
        index = 0                                                               # Find FreeListNode s.t. have enough space (get index and base of Node)
        found = 0
        curr = self.freelist.head.next
        while curr != self.freelist.head :
            if curr.bound >= size :
                found = 1
                break
            else :
                index += 1
                curr = curr.next

        if found :                                                              # If found space, initialize base
            base = curr.base
        else :                                                                  # If not found space, allocate one more chunk and initialize base and index
            self.chunk_cnt += 1
            self.free_size += self.chunk_size
            self.freelist.chunk_allocation(self.chunk_size, self.chunk_cnt)
            curr = self.freelist.getNode(-1)
            
            base = curr.base
            index = -1
            
        self.object_dic[id] = (base, size)                                      # Create Object info for object_dic (key = id, value = (base, size))\

        self.freelist.change_info(index, size, -size)                           # Change base and bound of the FreeListNode (base += size, bound -= size)
        self.used_size += size
        self.free_size -= size

    def free(self, id):        
        temp = self.object_dic.pop(id)                                          # Get info related with id
        base = temp[0]
        bound = temp[1]
        self.used_size -= bound
        self.free_size += bound

        index = 0                                                               # Insert New Node s.t. base and bound are obtained from above at appropriate position
        if base > self.freelist.getNode(index).base :
            index = self.freelist.find_index(base)  
        self.freelist.insert(index, base, bound)

        curr = self.freelist.merge(index)                                       # Verify Merging the Node is possible with previous or next Node And Merge

        self.freelist.chunk_deallocation(curr, self.chunk_size, self.chunk_cnt) # Chunk de-allocation
        
if __name__ == "__main__":
    a = time.time()
    allocator = Allocator()
    with open ("./input_origin.txt", "r") as file:
        alloc_t_sum = 0
        free_t_sum = 0
        alloc_max = -1; alloc_min = 1
        free_max = -1; free_min = 1
        for line in file:
            req = line.split()
            if req[0] == 'a':      
                # print("=======malloc=======")
                # print(f"  id = {int(req[1])}")
                # print(f"size = {int(req[2])}")                          
                alloc_s = time.time()
                allocator.malloc(int(req[1]), int(req[2]))
                alloc_f = time.time()
                if (alloc_f - alloc_s) > alloc_max :
                    alloc_max = alloc_f - alloc_s
                if (alloc_f - alloc_s) < alloc_min :
                    alloc_min = alloc_f - alloc_s
                alloc_t_sum += (alloc_f - alloc_s)
            elif req[0] == 'f':
                # print("========free========")
                # print(f"  id = {int(req[1])}")
                # print(f"size = {allocator.object_dic[int(req[1])][1]}")                               
                free_s = time.time()
                allocator.free(int(req[1]))
                free_f = time.time()
                if (free_f - free_s) > free_max :
                    free_max = free_f - free_s
                if (free_f - free_s) < free_min :
                    free_min = free_f - free_s
                free_t_sum += (free_f - free_s)
                        

    b = time.time()

    allocator.print_stats()
    with open ("./output_ff.txt", "w") as file :
        allocator.freelist.print_list_to_file(file)
    print("Allocation Time Spent Mean :", f"{float(alloc_t_sum / 100000):.7f} sec")
    print("Allocation Time Spent Max  :", f"{alloc_max:.7f} sec")
    print("Allocation Time Spent Min  :", f"{alloc_min:.7f} sec")
    print("   Free    Time Spent Mean :", f"{float(free_t_sum / 16704):.7f} sec")
    print("   Free    Time Spent Max  :", f"{free_max:.7f} sec")
    print("   Free    Time Spent Min  :", f"{free_min:.7f} sec")
    # print("Time spent :", int(alloc_t_sum + free_t_sum) ,"sec")
    print("Time spent :", int(b - a) ,"sec")