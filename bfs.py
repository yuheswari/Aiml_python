# Define the graph as an adjacency list
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

# BFS function
def bfs(visited, graph, start_node):
    visited = []  # List to keep track of visited nodes
    queue = []    # Initialize a queue

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        # Pop the first node from the queue
        current_node = queue.pop(0)
        print(current_node, end=" ")

        # Explore all neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Perform BFS starting from node '5'
print("BFS Traversal:")
bfs([], graph, '5')
