#!/bin/python3

# Given a adjacency matrix find the number of islands (Number of 1's)
# that are neighbors from each other.

# Find neighbors
def find_neighbors(matrix, current, visited):
    """current is a tuple of (x,y) coordinates."""
    neighboors = []
    m = matrix
    x, y = current
    print("Finding neighbors of x:" + str(x) + " y: " + str(y))

    # Check top row
    for i in range(-1, 2):
        if (x-1 >= 0 and x-1 < len(m) and y+i >= 0 and y+i < len(m[0])):
            n = (x-1, y+i)  # Neighbor
            if (n not in visited and m[n[0]][n[1]] == [1]):
                visited.add(n)
                neighboors.append(n)
    for i in range(-1, 2):
        if (x >= 0 and x < len(m) and y+i >= 0 and y+i < len(m[0])):
            n = (x, y+i)  # Neighbor
            if n not in visited and m[n[0]][n[1]] == [1]:
                visited.add(n)
                neighboors.append(n)
    for i in range(-1, 2):
        if (x+1 >= 0 and x+1 < len(m) and y+i >= 0 and y+i < len(m[0])):
            n = (x+1, y+i)  # Neighbor
            if (n not in visited and m[n[0]][n[1]] == [1]):
                visited.add(n)
                neighboors.append(n)
    return neighboors


def getIslands(matrix):
    islands = 0
    visited = set()
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            islands += dfs(matrix, (r,c), visited)
    return islands

def dfs(matrix, current, visited):
    print("BFS - current: {} visited nodes: {}".format(str(current), visited))
    Q = []
    Q.append(current)
    found_island = 0
    while Q != []:
        current = Q.pop(0)
        x,y = current
        # if matrix[x][y] == [1]:
        #     print("FOUND A 1")
        # print("Current in QUEUE " + str(current))
        # print("IS CURRENT 1? : " + str(matrix[x][y][0]))
        if current not in visited and matrix[x][y] == [1]:
            visited.add(current)
            found_island = 1
            print("Found island at: " + str(current))
            for neighbor in find_neighbors(matrix, current, visited):
                Q.append(neighbor)
    return found_island

# print matrix
def print_matrix(matrix):
    """Prints a 2D matrix."""
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end="")
        print()

matrix = [
    [[0],[1],[1],[0],[1]],
    [[0],[0],[1],[0],[0]],
    [[1],[0],[0],[0],[0]],
    [[0],[0],[0],[1],[1]],
    [[0],[1],[0],[0],[0]]]

is_land = getIslands(matrix)
print(is_land)
