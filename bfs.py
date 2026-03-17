from collections import deque

# Function for BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Taking input from user
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start_node = input("Enter starting node: ")

# Run BFS
bfs(graph, start_node)