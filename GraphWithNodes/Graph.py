'''graph.py'''


class Node(object):
    '''a node'''

    def __init__(self, value, identifier):
        self._value = value
        self._identifier = identifier

    @property
    def value(self):
        '''get value'''
        return self._value

    @property
    def identifier(self):
        '''id'''
        return self._identifier

    def print_info(self):
        '''get info'''
        print "ID:", self._identifier, "Value:", self._value


class Graph(object):
    '''the graph'''

    def __init__(self, dims):
        cols = dims[0]
        rows = dims[1]
        self._nodes = {}
        for i in range(0, cols):
            for j in range(0, rows):
                nodekey = str(i), ',', str(j)
                self._nodes[nodekey] = Node([i, j], len(self._nodes))

    def nodes(self):
        '''get nodes'''
        return self._nodes

    def get_node(self, node):
        '''get a node'''
        nodekey = str(node[0]), ',', str(node[1])
        if nodekey in self._nodes:
            return self._nodes[nodekey]
        return None


def get_neighbors(node, graph):
    '''Gets the neighbors of the given node within the given graph'''
    right = [1, 0]
    top = [0, 1]
    left = [-1, 0]
    down = [0, -1]
    dirs = [right, top, left, down]
    neighbors = []
    for i in dirs:
        nodekey = [node.value[0] + i[0], node.value[1] + i[1]]
        if graph.get_node(nodekey):
            neighbors.append(graph.get_node(nodekey))

    return neighbors


def test_graph():
    '''abc'''
    graph = Graph([3, 3])
    n = graph.get_node([1, 1])
    nays = get_neighbors(n, graph)
    for i in nays:
        i.print_info()


if __name__ == "__main__":
    print "Graph"
    test_graph()
