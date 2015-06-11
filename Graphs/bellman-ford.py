__author__ = 'alex'

# Finds shortest path (SP) for directed graph without negative-sum cycles

graph = {
    'a' : {'b' : 10, 'c' : 6},
    'b' : {'d' : 5},
    'c' : {'b' : 2},
    'd' : {}
}

def bellman_ford(graph, start_node):
    N = len(graph)
    sps = dict.fromkeys(graph.keys(), 'inf')
    sps[start_node] = 0
    print sps

    for i in xrange(N):
        # RELAX (for each edge)
        for start in graph.keys():
            adjacent_nodes = graph[start]
            for end in adjacent_nodes.keys():
                if sps[end] > sps[start] + adjacent_nodes[end]:
                    sps[end] = sps[start] + adjacent_nodes[end]
                    print sps

bellman_ford(graph, 'a')
