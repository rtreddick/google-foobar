from challenge_5_bfs_OLD import solution as bfs_solution_OLD
from challenge_5_bfs import solution as bfs_solution_optimized

# testing empty grids

def test_zeros(h, w):
    return [[0 for n in range(w)] for m in range(h)]

def test_zeros_square(s):
    return test_zeros(s, s)

test_case_1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
test_case_2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
test_case_3 = [
    [0,0,0,0],
    [1,1,1,0],
    [1,1,1,0],
    [1,1,1,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,0,1],
    [0,1,0,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [0,1,0,1],
    [0,1,0,1],
    [0,1,0,0],
    [0,1,1,0],
    [0,1,1,0],
    [0,0,0,0]
]
test_case_4 = test_zeros(20,11)
test_case_5 = test_zeros(20,20)

# print(f"test_case_1: {bfs_solution_optimized(test_case_1)}")
# print(f"test_case_2: {bfs_solution_optimized(test_case_2)}")
print(f"test_case_3: {bfs_solution_optimized(test_case_3)}")
print(f"test_case_4: {bfs_solution_optimized(test_case_4)}")





