from codetiming import Timer

@Timer()
def solution(map):

    def _build_graph(map):

        graph = {}
        w = len(map[0])
        l = len(map)

        for m, row in enumerate(map):
            for n, wall in enumerate(row):
                children = tuple(
                    node for node in [
                        (m, n + 1), # right
                        (m + 1, n), # down
                        (m, n - 1), # left
                        (m - 1, n) # up
                    ] if (
                        0 <= node[0] <= w - 1 and
                        0 <= node[1] <= l - 1
                    )
                )
                graph.update({(m, n): {"children": children, "wall": wall}})

        return graph, (w-1, l-1)

    def _bfs(graph, end):

        # build queue of paths to explore, track number of walls removed for each path
        path_queue = [{"path": [(0,0)], "walls_removed": 0}]
        while len(path_queue) != 0:
            current_path = path_queue.pop(0)
            last_node = current_path["path"][-1]

            # when bfs reaches end, we've found the shortest path length
            if last_node == end:
                return len(current_path["path"])

            # iterate through all children of last_node
            for child in graph[last_node]["children"]:

                # don't pass the same node twice
                if child not in current_path["path"]:

                    # only explore wall nodes if we haven't yet removed a wall
                    if graph[child]["wall"] == 1 and current_path["walls_removed"] == 0:

                        # add path to queue, update walls_removed to 1
                        path_queue.append({
                            "path": current_path["path"] + [child],
                            "walls_removed": 1})

                    # explore all passable nodes
                    elif graph[child]["wall"] == 0:
                        path_queue.append({
                            "path": current_path["path"] + [child],
                            "walls_removed": current_path["walls_removed"]
                        })
    
    graph, end = _build_graph(map)

    return _bfs(graph, end)