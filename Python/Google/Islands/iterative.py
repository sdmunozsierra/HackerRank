# Given a adjacency matrix find the number of islands (Number of 1's)
# that are neighbors from each other.

# Find neighbors
def find_neighbors(matrix, current, visited):
    """Find the neighbors of current that have not being visited.
    :param matrix: matrix to be used.
    :param current: tuple of (x,y) coordinates.
    :param visited: set of visited coordinates."""
    # Placeholder variables
    m = matrix
    x, y = current
    neighbors = []  # Found neighbors
    # print("Finding neighbors of x:" + str(x) + " y: " + str(y))  # debugging

    # Iterate through each possible row. Top, Middle, Bottom.
    for i in range(-1, 2):  # Check column -1, column, column +1
        # Check top row
        if (x-1 >= 0 and x-1 < len(m) and y+i >= 0 and y+i < len(m[0])):
            n = (x-1, y+i)  # Generated neighbor
            # if not visited and equals to 1
            if (n not in visited and m[n[0]][n[1]] == [1]):
                # Valid neighbor n
                visited.add(n)  # Mark as visited
                neighbors.append(n)  # Add to possible neighbors

    for i in range(-1, 2):
        # Check middle row
        if (x >= 0 and x < len(m) and y+i >= 0 and y+i < len(m[0])):
            n = (x, y+i)
            if n not in visited and m[n[0]][n[1]] == [1]:
                visited.add(n)
                neighbors.append(n)

    for i in range(-1, 2):
        # Check bottom row
        if (x+1 >= 0 and x+1 < len(m) and y+i >= 0 and y+i < len(m[0])):
            n = (x+1, y+i)
            if (n not in visited and m[n[0]][n[1]] == [1]):
                visited.add(n)
                neighbors.append(n)
    # Return list of valid neighbors
    return neighbors


def getIslands(matrix):
    """Get number of islands according to a 2D matrix."""
    islands = 0  # Total islands
    visited = set()  # Visited coordinates

    # Iterate through the whole matrix
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            # Record how many islands have we seen
            islands += dfs(matrix, (r,c), visited)
    return islands

def dfs(matrix, current, visited):
    """Runs Breadth First Search in the matrix from current coordinates.
    :param matrix: matrix to be searched.
    :param current: tuple for coordinates (x,y) to start the algorithm from.
    :param visited: set of visited coordinates (x,y)."""
    # print("BFS - current: {} visited nodes: {}".format(str(current), visited))
    # Create a queue from the starting coordinates.
    queue = []
    queue.append(current)
    found_island = 0  # new islands were found
    while queue != []:
        current = queue.pop(0)  # pop from queue
        x,y = current
        # Check that the current coordinates have not been visited or != 0
        if current not in visited and matrix[x][y] == [1]:
            visited.add(current)
            found_island = 1
            # Find neighbors for current coordinates
            for neighbor in find_neighbors(matrix, current, visited):
                queue.append(neighbor)  # Add valid neighbors to queue
    return found_island

# print matrix
def print_matrix(matrix):
    """Prints a 2D matrix."""
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c], end="")
        print()

def main():
    """Runs getIslands against a matrix."""

    # Matrix to be used
    matrix = [
        [[0],[1],[1],[0],[1]],
        [[0],[0],[1],[0],[0]],
        [[1],[0],[0],[0],[0]],
        [[0],[0],[0],[1],[1]],
        [[0],[1],[0],[0],[0]]]

    # Get number of islands of matrix
    number_of_islands = getIslands(matrix)
    print("There are {} islands in Matrix:".format(str(number_of_islands)))
    print_matrix(matrix)


main()
