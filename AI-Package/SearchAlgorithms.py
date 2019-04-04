import math
from queue import *


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
        cost_count = 0
        self.row_count = 0
        self.column_count = 0
        self.grid = list()
        row = list()
        for symbol in mazeStr:
            if symbol == ',':
                continue
            if symbol == ' ':
                self.row_count += 1
                self.column_count = 0
                self.grid.append(row.copy())
                row.clear()
            else:
                node = Node(symbol)
                node.id = (self.row_count, self.row_count)
                node.gOfN = 0.0
                node.heuristicFn = 1000.0

                if edgeCost:
                    node.edgeCost = edgeCost[cost_count]
                if symbol == 'S':
                    self.start = node
                if symbol == 'E':
                    node.hOfN = 0.0
                    self.goal = node
                row.append(node)
                cost_count += 1
                self.column_count += 1
        self.grid.append(row.copy())
        self.row_count += 1  # for the last row, because there won't be a space
        for n in range(0, self.row_count):
            for m in range(0, self.column_count):
                if n - 1 in range(0, self.row_count):
                    self.grid[n][m].up = self.grid[n - 1][m].id
                if n + 1 in range(0, self.row_count):
                    self.grid[n][m].down = self.grid[n + 1][m].id
                if m - 1 in range(0, self.column_count):
                    self.grid[n][m].left = self.grid[n][m - 1].id
                if m + 1 in range(0, self.column_count):
                    self.grid[n][m].right = self.grid[n][m + 1].id

        '''for ROW in self.grid:
            for NODE in ROW:
                print(NODE.value)'''

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
        # set all nodes to infinity
        self.path.clear()
        self.fullPath.clear()
        self.totalCost = -1

        for i in range(0, self.row_count):
            for j in range(0, self.column_count):
                self.grid[i][j].gOfN = 1e9

        pq = PriorityQueue()
        visited = list()
        self.grid[0][0].gOfN = 0
        pq.put((0, self.grid[0][0]))
        while not pq.empty():
            tmp = pq.get()
            # currentCost = tmp[0]
            currentNode = tmp[1]
            visited.append(currentNode)

            if currentNode == self.goal:
                self.totalCost = currentNode.gOfN
                while currentNode.previousNode:
                    self.path.append(self.get_1D_idx(currentNode.id[0], currentNode.id[1]))
                    currentNode = currentNode.previousNode
                self.path.append(self.get_1D_idx(currentNode.id[0], currentNode.id[1]))
                for n in visited:
                    self.fullPath.append(self.get_1D_idx(n.id[0], n.id[1]))
                self.path.reverse()
                break

            # The order of expanding node’s children will be (up, down, left, right).
            if currentNode.up is not None:
                node = self.grid[currentNode.up[0]][currentNode.up[1]]
                if node.gOfN > node.edgeCost + currentNode.gOfN:  # old_minimum > new cost
                    node.gOfN = node.edgeCost + currentNode.gOfN  # update the minimum
                    node.previousNode = currentNode               # update Parent
                    pq.put((node.gOfN, node))                     # push the child in the PQ
                    self.grid[currentNode.up[0]][currentNode.up[1]] = node

            if currentNode.down is not None:
                node = self.grid[currentNode.down[0]][currentNode.down[1]]
                if node.gOfN > node.edgeCost + currentNode.gOfN:
                    node.gOfN = node.edgeCost + currentNode.gOfN
                    node.previousNode = currentNode
                    pq.put((node.gOfN, node))
                    self.grid[currentNode.down[0]][currentNode.down[1]] = node

            if currentNode.left is not None:
                node = self.grid[currentNode.left[0]][currentNode.left[1]]
                if node.gOfN > node.edgeCost + currentNode.gOfN:
                    node.gOfN = node.edgeCost + currentNode.gOfN
                    node.previousNode = currentNode
                    pq.put((node.gOfN, node))
                    self.grid[currentNode.left[0]][currentNode.left[1]] = node

            if currentNode.right is not None:
                node = self.grid[currentNode.right[0]][currentNode.right[1]]
                if node.gOfN > node.edgeCost + currentNode.gOfN:
                    node.gOfN = node.edgeCost + currentNode.gOfN
                    node.previousNode = currentNode
                    pq.put((node.gOfN, node))
                    self.grid[currentNode.right[0]][currentNode.right[1]] = node
        return self.path, self.fullPath, self.totalCost


    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.path.clear()
        self.fullPath.clear()
        self.totalCost = -1

        Nodes = list()         # list of unvisited nodes
        Visited = list()      # list of visited nodes
        self.grid[0][0].heuristicFn = 0.0
        Current = self.grid[0][0]    # current node
        Nodes.append(Current)      # add the current node to the unvisited nodes list
        while Nodes:
            Current = min(Nodes, key=lambda i:i.hOfN)
            Nodes.remove(Current)
            Visited.append(Current)
            """print("Current::\nid:", '({:d},{:d})'.format(Current.id[0], Current.id[1]))
            print("hOfN: ", Current.hOfN)
            print("gOfN: ", '{:f}'.format(Current.gOfN))
            print("huresticFN: ", '{:f}\n'.format(Current.heuristicFn))"""
            if Current == self.goal:
                self.totalCost = Current.gOfN
                while Current.previousNode:
                    self.path.append(self.get_1D_idx(Current.id[0], Current.id[1]))
                    Current = Current.previousNode
                self.path.append(self.get_1D_idx(Current.id[0], Current.id[1]))
                for n in Visited:
                    self.fullPath.append(self.get_1D_idx(n.id[0], n.id[1]))
                self.path.reverse()
                return self.path, self.fullPath, self.totalCost
            for Row in self.grid:
                for n in Row:
                    if Current.up == n.id or Current.down == n.id or Current.left == n.id or Current.right == n.id:
                        if n in Visited or n.value == '#':
                            continue
                        """print("new node::\nid:", '({:d},{:d})'.format(n.id[0], n.id[1]))
                        print("hOfN: ", n.hOfN)
                        print("gOfN: ", '{:f}'.format(n.gOfN))
                        print("huresticFN: ", '{:f}\n'.format(n.heuristicFn))"""
                        if n in Nodes:
                            #print("In Nodes\n")
                            nGOfN = float(Current.gOfN) + float(Current.edgeCost)
                            if nGOfN < n.gOfN:
                                n.gOfN = nGOfN
                                n.previousNode = Current
                        else:
                            #print("Not in Nodes")
                            n.gOfN = float(Current.gOfN) + float(Current.edgeCost)
                            n.hOfN = math.sqrt(float((n.id[0] - self.goal.id[0])*(n.id[0] - self.goal.id[0])) +
                                               float((n.id[1] - self.goal.id[1])*(n.id[1] - self.goal.id[1])))
                            n.heuristicFn = n.gOfN + float(n.hOfN)
                            n.previousNode = Current
                            """print("edgeCost: ", Current.edgeCost)
                            print("hOfN: ", n.hOfN)
                            print("gOfN: ", '{:f}'.format(n.gOfN))
                            print("huresticFN: ", '{:f}\n'.format(n.heuristicFn))"""
                            Nodes.append(n)

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

    #searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
