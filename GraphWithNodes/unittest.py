'''Unit testing for astar algorithim'''

from Astar import Grid
from Astar import AStar

def unit_test():
    '''unit test'''
    print "\nBegin unit test\n"
    grid = Grid([10, 10])
    grid.print_info()

    astar = AStar()
    astar.pathfind(grid.nodelist[0], grid.nodelist[99])


if __name__ == "__main__":
    unit_test()
