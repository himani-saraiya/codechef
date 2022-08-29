from itertools import *
K, M = map(int, input().split())

list1 = []
for _ in range(K):
    map_val = map(int, input().split())
    lst = list(map_val)[1:]
    list1.append(lst)
    N = list(product(*list1))
    list2= []

max_result = -1
for cartesian_arr in N:
    sum_squared = sum(map(lambda x: x**2, cartesian_arr))
    result = sum_squared % M
    list2.append(result)

max_result = max(list2)
print(max_result)