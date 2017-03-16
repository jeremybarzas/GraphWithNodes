'''AStar algorithim'''

class Node(object):
    '''Node object'''

    def __init__(self, pos):
        '''node constructor'''
        self.position = pos
        self.gCost = 0
        self.hCost = 0
        self.fCost = 0
        self.walkable = True
        self.parent = None
        self.neighbors = []
        self.grid_index = 0

    def set_neighbors(self, grid):
        '''get neighbors for a node'''
        right = [1, 0]
        top_right = [1, 1]
        top = [0, 1]
        top_left = [-1, 1]
        left = [-1, 0]
        bottom_left = [-1, -1]
        bottom = [0, -1]
        bottom_right = [1, -1]
        dirs = [right, top_right, top, top_left, left, bottom_left, bottom, bottom_right]
        for i in dirs:
            item1 = i[0] + self.position[0]
            item2 = i[1] + self.position[1]
            fetch_node = grid.get_node([item1, item2])
            if fetch_node:
                self.neighbors.append(fetch_node)

    def print_info(self):
        '''print info'''
        print "ID: " + str(self.grid_index) + "  Position: " + str(self.position[0]) + ',' + str(self.position[1])


class Grid(object):
    '''Grid object'''

    def __init__(self, size):
        '''constructor'''
        cols = size[0]
        rows = size[1]
        self.nodelist = []
        for i in range(0, cols):
            for j in range(0, rows):
                self.nodelist.append(Node([i, j]))
        for node in self.nodelist:
            node.grid_index = self.nodelist.index(node)
            node.set_neighbors(self)

    def get_node(self, searchfor):
        '''get a node by list [1,1]'''
        for node in self.nodelist:
            if node.position == searchfor:
                return node

    def print_info(self):
        '''print node'''
        for node in self.nodelist:
            node.print_info()


class AStar(object):
    '''AStar algorithim'''

    def __init__(self):
        '''constructor'''

    def manhattan_distance(self, start, goal):
        '''manhattan distance heuristic'''
        x_dif = abs(start.position[0] - goal.position[0])
        y_dif = abs(start.position[1] - goal.position[1])
        return x_dif + y_dif

    def pathfind(self, start, goal):
        '''the astar search algorithim'''
        print "\nStart Node:" # DEBUG STUFF
        start.print_info() # DEBUG STUFF
        print "Goal Node:" # DEBUG STUFF
        goal.print_info() # DEBUG STUFF
        openlist = []
        closedlist = []
        current = start
        openlist.append(current)
        while openlist.count != 0:
            openlist.sort(key=lambda x: x.fCost)
            current = openlist[0]
            if current == goal:
                print "\nCurrent Node: " # DEBUG STUFF
                current.print_info() # DEBUG STUFF
                closedlist.reverse()
                return self.retrace(closedlist, current)
            openlist.remove(current)
            closedlist.append(current)
            for neighbor in current.neighbors:
                if closedlist.__contains__(neighbor):
                    continue
                tentative_gCost = current.gCost + neighbor.gCost
                if not openlist.__contains__(neighbor):
                    if neighbor.walkable:
                        openlist.append(neighbor)
                elif tentative_gCost >= neighbor.gCost:
                    continue
                neighbor.parent = current
                neighbor.gCost = tentative_gCost
                neighbor.hCost = self.manhattan_distance(neighbor, goal)
                neighbor.fCost = neighbor.gCost + neighbor.hCost
        return False

    def retrace(self, path, current):
        '''reconstructs the path'''
        print "Retrace has been called" # DEBUG STUFF
        print "\nPath that was taken:" # DEBUG STUFF
        for node in path: # DEBUG STUFF
            node.print_info() # DEBUG STUFF
