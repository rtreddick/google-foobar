from collections import Counter

def solution(n, b):

    def convert_to_str(n, b, k):
        result = []
        while n:
            result.append(str(n % b))
            n = n // b

        return ''.join(reversed(result)).zfill(k)

    k = len(n)
    x = ''
    node_1_list = []
    node_2_list = []

    while True:
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(x))
        z = convert_to_str(int(x, b) - int(y, b), b, k)
        node_1_list.append(n)
        node_2_list.append(z)
        if z in node_1_list:
            return len(node_2_list) - node_1_list.index(z)
        else:
            n = z

test_case_1 = ('210022', 3)
test_case_2 = ('1211', 10)

assert solution(*test_case_1) == 3
print("test_case_1 passed")

assert solution(*test_case_2) == 1
print("test_case_2 passed")