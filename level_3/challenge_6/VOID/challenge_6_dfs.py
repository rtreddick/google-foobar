# def solution(l):

#     # build graph
#     graph = {}
#     l = list(enumerate(l))
#     for node in l:
#         # graph.update({node:[edge_node for edge_node in l[node[0]+1:] if edge_node[1] % node[1] == 0]})
#         graph.update({node:[edge_node for edge_node in l[node[0]+1:] if edge_node[1] % node[1] == 0]})

#     # memo to store paths
#     memo = {}

#     # search graph to depth 3
#     depth = 3
#     path_queue = [[key] for key in graph.keys()]
#     while len(path_queue) != 0:
#         current_path = path_queue.pop()
#         current_node = current_path[-1]
#         for edge_node in graph[current_node]:
#             new_path = current_path + [edge_node]
#             if len(new_path) == depth:
#                 path_memo = tuple(node[1] for node in new_path)
#                 if not memo.get(path_memo):
#                     memo.update({path_memo:1})
#             else:
#                 path_queue.append(new_path)

#     return len(memo)

# test_case = [1]*2000
# result = solution(test_case)
# print(result)

