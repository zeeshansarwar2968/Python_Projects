# li1 = ['geek']
# n = 5  #Number of time loop runs
# for i in range(int(n)):
#     li1 = [li1]
#     print(li1)
import functools
import itertools
import copy
list1 = [1,2,3,4,5,6,1,2,[1,2]]

sample_list = ['About', 'Absolutely', 'After', 'Aint', 'Alabama', 'AlabamaBill', 'All', 'Also', 'Amos', 'And',
               'Anyhow', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam', 'Behind', 'Besides', 'Biblical', 'Bill',
               'Billgone']

dict1 = {}

for i in sample_list:
    f = i[0]
    if f in dict1.keys(): dict1[f].append(i)
    else: dict1[f] = [i]

print(dict1)