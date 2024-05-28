obj_dic = {}
with open ("./input.txt", "r") as file:
        a_sum = 0; a_c = 0
        f_sum = 0; f_c = 0
        for line in file:
            req = line.split()
            if req[0] == 'a':
                a_c += 1
                a_sum += int(req[2])
                obj_dic[int(req[1])] = int(req[2])
            if req[0] == 'f':
                f_c += 1
                f_sum += obj_dic[int(req[1])]

print("# of a =", a_c,", # of f =", f_c)
print("a_sum =",a_sum,", f_sum =", f_sum)
print("in-use :", a_sum - f_sum)
            
