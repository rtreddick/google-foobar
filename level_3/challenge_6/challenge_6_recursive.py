from codetiming import Timer
from numpy.random import default_rng

def solution(l):

    def _build_graph(l):
        l = list(enumerate(l))
        return {node:[edge for edge in l if edge[0] > node[0] and edge[1] % node[1] == 0] for node in l}

    def _recursive(node, depth):
        
        # base cases
        if depth =

    graph = _build_graph(l):

    for node in graph:

        _recursive(node)