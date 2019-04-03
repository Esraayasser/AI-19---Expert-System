import math


class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    goal = Node('E')

    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        k = 0
        self.i = 0
        self.j = 0
        self.grid = list()
        row = list()
        for c in mazeStr:
            if c == ',':
                continue
            if c == ' ':
                self.i += 1  # row gdied ya-4paap
                self.j = 0
                self.grid.append(row.copy())
                row.clear()
            else:
                n = Node(c)
                n.id = (self.i, self.j)
                n.gOfN = 0
                n.hOfN = 1e9
                n.heuristicFn = 1e9

                if edgeCost:
                    n.edgeCost = edgeCost[k]
                if c == 'E':
                    n.hOfN = 0
                    self.goal = n
                row.append(n)
                k += 1
                self.j += 1
        self.grid.append(row.copy())
        self.i += 1  # row gdied ya-4paap
        for n in range(0, self.i):
            for m in range(0, self.j):
                if n - 1 in range(0, self.i):
                    self.grid[n][m].up = self.grid[n - 1][m].id
                if n + 1 in range(0, self.i):
                    self.grid[n][m].down = self.grid[n + 1][m].id
                if m - 1 in range(0, self.j):
                    self.grid[n][m].left = self.grid[n][m - 1].id
                if m + 1 in range(0, self.j):
                    self.grid[n][m].right = self.grid[n][m + 1].id
        #pass

    def get_1D_idx(self, r, c):
        return r * self.j + c

    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath

    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath

    def UCS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost

    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        Nodes = set()         # list of unvisited nodes
        Visited = list()      # list of visited nodes
        self.grid[0][0].heuristicFn = 0
        Current = self.grid[0][0]    # current node
        Nodes.add(Current)      # add the current node to the unvisited nodes list
        while Nodes:
            Current = min(Nodes, key=lambda i:i.heuristicFn)
            if Current == self.goal:
                self.totalCost = Current.gOfN
                while Current.previousNode:
                    self.path.append(self.get_1D_idx(Current.id[0], Current.id[1]))
                    Current = Current.previousNode
                self.path.append(self.get_1D_idx(Current.id[0], Current.id[1]))
                for n in Visited:
                    self.fullPath.append(self.get_1D_idx(n.id[0],n.id[1]))
                return self.path, self.fullPath, self.totalCost
            Nodes.remove(Current)
            Visited.append(Current)
            for Row in self.grid:
                for n in Row:
                    if Current.up == n.id or Current.down == n.id or Current.left == n.id or Current.right == n.id:
                        if n in Visited or n.value == '#':
                            continue
                        if n in Nodes:
                            nGOfN = Current.gOfN + Current.edgeCost
                            if nGOfN < n.gOfN:
                                n.gOfN = nGOfN
                                n.previousNode = Current
                        else:
                            n.gOfN = Current.gOfN + Current.edgeCost
                            n.hOfN = math.sqrt(((n.id[0] - self.goal.id[0])*(n.id[0] - self.goal.id[0])) +
                                               ((n.id[1] - self.goal.id[1])*(n.id[1] - self.goal.id[1])))
                            n.heuristicFn = n.gOfN + n.gOfN
                            n.previousNode = Current
                            Nodes.add(n)

        return self.path, self.fullPath, self.totalCost

    def AStarManhattanHeuristic(self):
        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost


def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
               #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

            #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
