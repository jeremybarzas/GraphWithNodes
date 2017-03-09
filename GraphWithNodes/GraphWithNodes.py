class Node:
    '''The Node object'''
    def __init__(self, val, id):
        self.value = val
        self.identifier = id

class Graph:   
    ''' The Graph object'''     
    def __init__(self, n):
        self.nodes = n                
    def getnode(self, id):
        ''' Returns the node with the given id'''       
        for node in self.nodes:
            if node.identifier == id:
                return node.identifier
        return "Node Not Found"
                
def main():
    ''' main body function'''
    nodelist = [Node('A', 0), Node('B', 1), Node('C', 2), Node('D', 3), Node('E', 4), Node('F', 5), Node('G', 6), Node('H', 7), Node('I', 8)]
    graph = Graph(nodelist)
    print graph.getnode(0)
    print graph.getnode(1)
    print graph.getnode(2)
    print graph.getnode(3)
    print graph.getnode(4)
    
if __name__ == "__main__":
    print "\nThis is the main function\n"
    main()