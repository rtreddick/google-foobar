from collections import Counter

def solution(data, n):
    counter = Counter(data)
    return [id for id in data if counter.get(id) <= n]

test_case_1 = ([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
test_case_2 = ([1, 2, 3], 0)

assert solution(*test_case_1) == [1,4]
print("test_case_1 succeeded")

assert solution(*test_case_2) == []
print("test_case_2 succeeded")