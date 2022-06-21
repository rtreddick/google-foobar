from codetiming import Timer

from challenge_5_bfs_OLD import solution as solution_OLD

@Timer()
def solution(map):
    '''
    Took a BFS approach. First attempt had exponential time complexity, but
    I figured out how to memoize nodes already visited to only pursue paths that are candidates for shortest path.
    This solution easily generalizes to allowing more walls to be removed.
    Inner _bfs function already has an argument for walls_allowed which works in my testing.
    Only have to modify outer solution function to take walls_allowed argument and pass to _bfs.
    '''

    def _build_graph(map):

        graph = {}
        w = len(map[0])
        l = len(map)

        for m, row in enumerate(map):
            for n, wall in enumerate(row):
                edges = tuple(
                    node for node in [
                        (m, n + 1), # right
                        (m + 1, n), # down
                        (m, n - 1), # left
                        (m - 1, n)  # up
                    ] if (
                        0 <= node[0] <= l - 1 and
                        0 <= node[1] <= w - 1
                    )
                )
                graph[(m, n)] = (edges, wall)

        return graph, (l-1, w-1)

    def _bfs(graph, end_node, walls_allowed):

        memo = {}

        # instantiate queue starting at origin
        # [(path, walls_removed), ...]
        path_queue = [([(0,0)], 0)]

        # while there are still paths to explore
        while len(path_queue) != 0:

            current_path, current_walls_removed = path_queue.pop(0)
            current_node = current_path[-1]

            # if current_node == end_node, shortest path length found
            if current_node == end_node:
                return len(current_path)

            # explore all edges
            edge_nodes = graph[current_node][0]
            for edge_node in edge_nodes:  

                # don't explore edge nodes already in the path
                if edge_node in current_path:
                    continue

                # only explore wall nodes if still able to remove a wall
                edge_node_wall = graph[edge_node][1]
                new_walls_removed = current_walls_removed + edge_node_wall
                if new_walls_removed > walls_allowed:
                    continue
                
                # check if edge_node has been visited before
                # memoized path length is guaranteed to be less than current path length (if visited in a prior generation)
                # or equal to current path length (if visitied this generation)
                # current path is only a candidate if edge_node reached with fewer walls removed (because impossible to be of shorter length)
                # the entire generation of paths is sorted to guarantee paths with fewer walls removed are visited first
                # only continue exploring this path if it is a valid candidate
                if memo.get(edge_node) is not None:
                    if new_walls_removed >= memo[edge_node]:
                        continue

                # if not visited yet or path is a better candidate, update memo
                memo[edge_node] = new_walls_removed

                # if algorithm reaches this step, append path to path_queue
                path_queue.append((current_path + [edge_node], new_walls_removed))

            # if starting a new generation sort path_queue by walls_removed
            # new generation indicated when next path is of greater length than current path
            if len(path_queue) > 1 and len(current_path) < len(path_queue[0][0]):
                path_queue.sort(key=lambda x: x[1])

    graph, end_node = _build_graph(map)
    walls_allowed = 1

    return _bfs(graph, end_node, walls_allowed)


############## TESTING ###############

def test_zeros(h, w):
    return [[0 for n in range(w)] for m in range(h)]

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
test_case = test_zeros(8,8)

print(f"optimized version: {solution(test_case)}")
print(f"old version: {solution_OLD(test_case)}")
