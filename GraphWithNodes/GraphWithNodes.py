'''node module to use '''


class Node(object):
    '''The Node object'''

    def __init__(self, idfier, val):
        self.identifier = idfier
        self.value = val

    def print_info(self):
        '''Print the Nodes info'''
        print "ID:", self.identifier, ", Value:", self.value


class Graph(object):
    ''' The Graph object'''

    def __init__(self, n, x, y):
        self.nodes = n
        self.xsize = x
        self.ysize = y


def get_node(idfier, graph):
    ''' Returns the node with the given id within the given graph'''
    for node in graph.nodes:
        if node.identifier == idfier:
            return node
    return Node(idfier, "No node with this id found.")


def get_neighbors(node, graph):
    '''Gets the neighbors of the given node within the given graph'''
    print "get_neighbors() was called."
    tmpnode = get_node(node.identifier, graph)


def main():
    ''' main body function'''
    print "This is the main function."
    nodelist = [Node(0, [0, 0]), Node(1, [0, 1]), Node(2, [0, 2]), Node(3, [1, 0]), Node(4, [1, 1]), Node(5, [1, 2]), Node(6, [2, 0]), Node(7, [2, 1]), Node(8, [2, 2])]
    graph = Graph(nodelist, 3, 3)
    node = get_node(0, graph)
    node.print_info()
    node = get_node(1, graph)
    node.print_info()
    node = get_node(2, graph)
    node.print_info()
    node = get_node(9, graph)
    node.print_info()

if __name__ == "__main__":
    print "GraphWithNodes"
    main()
