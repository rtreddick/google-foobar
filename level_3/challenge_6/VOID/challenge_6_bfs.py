def solution_1(l):

    graph = {}
    for i in l:
        graph.update({i:[j for j in l[l.index(i) + 1:] if j % i == 0]})

    depth = 3
    num_triples = 0
    path_queue = [[key] for key in graph.keys()]
    while len(path_queue) != 0:
        current_path = path_queue.pop(0)
        current_node = current_path[-1]
        for edge_node in graph[current_node]:
            new_path = current_path + [edge_node]
            if len(new_path) == depth:
                num_triples += 1
            else:
                path_queue.append(new_path)

    return num_triples

   
def solution(l):

    # build graph
    # l.sort() # I don't think we want to sort based on the instructions
    graph = {}
    for i in l:
        graph.update({i:[j for j in l[l.index(i) + 1:] if j % i == 0]})

    # testing
    print(graph)

    # search graph to depth 3
    depth = 3
    num_paths = 0
    path_queue = [[key] for key in graph.keys()]
    while len(path_queue) != 0:
        current_path = path_queue.pop(0)
        current_node = current_path[-1]
        for edge_node in graph[current_node]:
            new_path = current_path + [edge_node]
            if len(new_path) == depth:
                num_paths += 1
            else:
                path_queue.append(new_path)

    return num_paths

test_case = [1,2,3,4,5,6]
result = solution(test_case)
print(result)

test_case_2 = [1,1,1,2,4,8]
result = solution(test_case_2)
print(result)

