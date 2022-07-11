
from codetiming import Timer

############

# example
# [2,4,8,8,16,20]

# memo

# list
# [], [2], [4], [2,4], [8], [2,8], [4,8], [2,4,8], [8,8], [2,8,8], [4,8,8]
# [16], [2,16], [4,16], [2,4,16], [8,16], [2,8,16], [4,8,16], [8,8,16], [20], [2,20],
# [4,20], [2,4,20]

# codes
# [2,4,8], [2,8,8], [4,8,8], [2,4,16], [2,8,16], [4,8,16], [8,8,16], [2,4,20]

# @Timer()
# def solution_1(l):

#     codes = [[]]
#     while len(l) != 0:
#         num = [l.pop(0)]
#         codes.extend(
#             [code + num for code in codes if 
#                 (code + num not in codes) and
#                 (
#                   len(code + num) == 1 or
#                   (1 < len(code + num) <= 3 and num[0] % code[-1] == 0) 
#                 )
#             ]
#         )
            
#     return len([code for code in codes if len(code) == 3])

# #######################

# @Timer()
# def solution_2(l):

#     depth = 3
#     lists = [[] for i in range(depth)]

#     while len(l) != 0:
#         num = l.pop(0)
#         for i in range(depth - 1, 0, -1):

#             lists[i].extend(
#                 [
#                     item + [num] for item in lists[i-1] if
#                     num % item[-1] == 0 and item + [num] not in lists[i]
#                 ]
#             )
        
#         if [num] not in lists[0]:
#             lists[0].extend([[num]])

#     return len(lists[depth-1])

# from numpy.random import default_rng
# rng = default_rng(seed=1)
# vals = list(rng.integers(1,100,1000))
# vals2 = vals.copy()

# result = solution_1(vals)
# print(result)

# result_2 = solution_2(vals2)
# print(result_2)

#################


@Timer()
def solution(l):

    depth = 3
    lists = [[] for i in range(depth)]

    while len(l) != 0:
        num = l.pop(0)
        for i in range(depth - 1, 0, -1):

            lists[i].extend(
                [
                    item + [num] for item in lists[i-1] if
                    num % item[-1] == 0
                ]
            )
        
        lists[0].extend([[num]])

    return len(lists[depth-1])

from numpy.random import default_rng
rng = default_rng(seed=1)
vals = list(rng.integers(1,10,1000))
result = solution(vals)
print(result)



#######

# [1,1,1,1]

# [], [(1,0)], [(1,1)], [(1,0), (1,1)], [(1,2)], [(1,0), (1,2)], [(1,1), (1,2)], [(1,0), (1,1), (1,2)]
# [(1,3)], [(1,0), (1,3)], [(1,1), (1,3)], [(1,0), (1,1), (1,3)], [(1,2), (1,3)],
# [(1,0), (1,2), (1,3)], [(1,1), (1,2), (1,3)]


# @Timer()
# def solution(l):

#     codes = [[]]
#     while len(l) != 0:
#         num = [l.pop(0)]
#         codes.extend(
#             [code + num for code in codes if
#                 len(code + num) == 1 or
#                 (1 < len(code + num) <= 3 and num[0] % code[-1] == 0) 
#             ]
#         )
            
#     return len([code for code in codes if len(code) == 3])

# from numpy.random import default_rng
# rng = default_rng(seed=1)
# vals = list(rng.integers(1,100,1000))

# # # vals = [1,1,1]
# # # vals.sort()
# # vals = [1,2,4,1,2,4]
# result = solution(vals)
# print(result)
