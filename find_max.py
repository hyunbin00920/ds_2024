def find_max_recursive(list, n):
    if n == 1:
        return list[0]
    max_a = find_max_recursive(list, n - 1)
    return max(max_a, list[n - 1])        

def find_max_iterative(list):
    i = 0
    max = list[i]
    for i in range(1,10) :
        if (max < list[i]) :
            max = list[i]
    return max

list = []
for i in range(10) :
    list.append(int(input()))

a = find_max_iterative(list)
b = find_max_recursive(list,10)
print("iterative result : ", a)
print("recursive result : ", b)