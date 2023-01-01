from codetiming import Timer
from numpy.random import default_rng


# this is what I submitted
# @Timer()
# def solution(l):

#     # build graph
#     l = list(enumerate(l))
#     graph = {node:[edge for edge in l if edge[0] > node[0] and edge[1] % node[1] == 0] for node in l}
    
#     # memo for number of triples at each node
#     memo = {}

#     # count paths to depth 3 starting at each node
#     for node in graph.keys():
#         memo.setdefault(node, sum([len(graph[edge]) for edge in graph[node]]))
        
#     # return num of triples
#     return sum(memo.values())


@Timer()
def solution(l):

    # build graph
    l = list(enumerate(l))
    graph = {node:[edge for edge in l if edge[0] > node[0] and edge[1] % node[1] == 0] for node in l}
    
    # memo for number of triples at each node
    num_triples = 0

    # count paths to depth 3 starting at each node
    for node in graph.keys():
        num_triples += sum([len(graph[edge]) for edge in graph[node]])
        
    # return num of triples
    return num_triples


rng = default_rng(seed=1)
vals = list(rng.integers(1,1000,2000))

# vals = [4,1,1,8,2,1,8,4]
result = solution(vals)
print(result)
