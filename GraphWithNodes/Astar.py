'''AStar algorithim'''

import drawablenode as dn

class AStar(object):
    '''AStar algorithim'''

    def __init__(self):
        '''constuctor'''

    # function A*(start, goal)
    def astar(self, start, goal):
        '''the astar search algorithim'''
        # The set of nodes already evaluated.
        # closedSet := {}
        closedset = []

        # The set of currently discovered nodes that are not evaluated yet.
        # Initially, only the start node is known.
        # openSet := {start}
        openset = []
        openset.append(start)

        # For each node, which node it can most efficiently be reached from.
        # If a node can be reached from many nodes, cameFrom will eventually contain the
        # most efficient previous step.
        # cameFrom := the empty map
        camefrom = []

        # For each node, the cost of getting from the start node to that node.
        # gScore := map with default value of Infinity
        gscore = []

        # The cost of going from start to start is zero.
        # gScore[start] := 0
        gscore[start] = 0

        # For each node, the total cost of getting from the start node to the goal
        # by passing by that node. That value is partly known, partly heuristic.
        # fScore := map with default value of Infinity
        fscore = []

        # or the first node, that value is completely heuristic.
        # fScore[start] := heuristic_cost_estimate(start, goal)
        fscore[start] = 0 # NEEDS TO BE CALCULATED CORRECTLY

        # while openSet is not empty
        while openset.count != 0:
            # current := the node in openSet having the lowest fScore[] value
            current = dn.DrawableNode([1, 1])

            # if current = goal
            if current == goal:
                # return reconstruct_path(cameFrom, current)
                return self.reconstruct_path(camefrom, current)

            # openSet.Remove(current)
            openset.remove(current)

            # closedSet.Add(current)
            closedset.append(current)

            # for each neighbor of current
            for neighbor in current.adjacents:
                # if neighbor in closedSet
                if closedset.__contains__(neighbor):
                    # Ignore the neighbor which is already evaluated.
                    # continue
                    continue

                # The distance from start to a neighbor
                # tentative_gScore := gScore[current] + dist_between(current, neighbor)
                tentative_gscore = 0 # NEEDS TO BE CALCULATED CORRECTLY

                # Discover a new node
                # if neighbor not in openSet
                if not openset.__contains__(neighbor):
                    # openSet.Add(neighbor)
                    openset.append(neighbor)
                # else if tentative_gScore >= gScore[neighbor]
                elif tentative_gscore >= neighbor.g:
                    # This is not a better path.
                    # continue
                    continue

                # This path is the best until now. Record it!
                # cameFrom[neighbor] := current
                camefrom[neighbor] = current

                # gScore[neighbor] := tentative_gScore
                gscore[neighbor] = tentative_gscore

                # fScore[neighbor] := gScore[neighbor] + heuristic_cost_estimate(neighbor, goal)
                fscore[neighbor] = 0 # NEEDS TO BE CALCULATED CORRECTLY

        # return failure
        return False

    # function reconstruct_path(cameFrom, current)
    def reconstruct_path(self, cameform, current):
        '''reconstructs the path'''
        # total_path := [current]
        total_path = []

        # while current in cameFrom.Keys:
        while cameform.__contains__(current):
            # current := cameFrom[current]
            current = cameform[current]

            # total_path.append(current)
            total_path.append(current)

        # return total_path
        return total_path
