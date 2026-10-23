"""
Experiment 1: Breadth First Search (BFS)
Aim: To implement Breadth First Search (BFS) algorithm using Python.
"""
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited.append(start)

    while queue:
        m = queue.popleft()
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

if __name__ == '__main__':
    print("Following is the Breadth-First Search:")
    bfs(graph, 'A')
    print()
