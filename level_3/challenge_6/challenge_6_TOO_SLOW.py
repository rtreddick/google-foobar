
from collections import deque

from codetiming import Timer
from numpy.random import default_rng


@Timer()
def solution_1(l):

    l = l.copy()
    depth = 3
    lists = [[] for i in range(depth)]

    while len(l) != 0:
        num = l.pop(0)
        for i in range(depth - 1, 0, -1):
            lists[i].extend([item + [num] for item in lists[i-1] if num % item[-1] == 0])
        lists[0].extend([[num]])

    return lists[depth-1], len(lists[depth-1])

rng = default_rng(seed=1)
vals = [int(num) for num in rng.integers(1,10,1000)]
# vals = [4,1,1,8,2,1,8,4]
result = solution_1(vals)
print(result)


#######

# optimization 1
# doesn't help

# @Timer()
# def solution_2(l):

#     l = deque(l)
#     depth = 3
#     lists = [[] for i in range(depth)]

#     while len(l) != 0:
#         num = l.popleft()
#         for i in range(depth - 1, 0, -1):
#             lists[i].extend([item + [num] for item in lists[i-1] if num % item[-1] == 0])
#         lists[0].extend([[num]])

#     return len(lists[depth-1])

#############

# optimization 2
# this does the wrong thing

# @Timer()
# def solution_3(l):

#     l = l.copy()
#     depth = 3
#     sets = [set() for i in range(depth)]

#     while len(l) != 0:
#         num = l.pop(0)
#         for i in range(depth - 1, 0, -1):
#             sets[i].update([item + (num,) for item in sets[i-1] if num % item[-1] == 0])
#         sets[0].update({(num,)})

#     return len(sets[depth-1])


#############

# optimization 3

# @Timer()
# def solution_4(l):

#     # create dict of factors
#     l_set = set(l)
#     factors = {}
#     for i in l_set:
#         factors_list = []
#         for j in l_set:
#             if i % j == 0:
#                 factors_list.append(j)
#         factors[i] = set(factors_list)

#     # create lists to store codes and code fragments
#     depth = 3
#     lists = [[] for i in range(depth)]

#     # build codes
#     while len(l) != 0:
#         num = l.pop(0)
#         for i in range(depth - 1, 0, -1):
#             lists[i].extend([item + (num,) for item in lists[i-1] if item[-1] in factors[num]])
#         lists[0].extend([(num,)])

#     return len(lists[depth-1])

#############

# optimization 4

# @Timer()
# def solution_5(l):

#     # create dict of factors
#     l_set = set(l)
#     factors = {}
#     for i in l_set:
#         factors_list = []
#         for j in l_set:
#             if i % j == 0:
#                 factors_list.append(j)
#         factors[i] = set(factors_list)

#     codes = [tuple()]
#     while len(l) != 0:
#         num = l.pop(0)
#         codes.extend(
#             [code + (num,) for code in codes if 
#                   len(code + (num,)) == 1 or
#                   (1 < len(code + (num,)) <= 3 and code[-1] in factors[num]) 
#             ]
#         )
            
#     return len([code for code in codes if len(code) == 3])





