"""

Adapted from Geeks4Geeks.org 

Origin URL: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

"""
from collections import deque

# Function to perform Breadth First Search on a graph
# represented using adjacency list
def bfs(adjList, startNode, visited):
    # Create a queue for BFS
    q = deque()

    # Mark the current node as visited and enqueue it
    visited[startNode] = True
    q.append(startNode)

    # Iterate over the queue
    while q:
        # Dequeue a vertex from queue and print it
        currentNode = q.popleft()
        print(currentNode, end=" ")

        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent has not been visited, then mark it visited and enqueue it
        for neighbor in adjList[currentNode]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)

# Function to add an edge to the graph
def addEdge(adjList, u, v):
    adjList[u].append(v)

def main():
    # Number of vertices in the graph
    vertices = 14

    # Adjacency list representation of the graph
    adjList = [[] for _ in range(vertices)]

    # Add edges to the graph
    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 0, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 1, 5)
    addEdge(adjList, 1, 6)
    addEdge(adjList, 4, 10)
    addEdge(adjList, 4, 11)
    addEdge(adjList, 6, 12)
    addEdge(adjList, 2, 7)
    addEdge(adjList, 2, 8)
    addEdge(adjList, 8, 13)
    addEdge(adjList, 3, 9)

    # Mark all the vertices as not visited
    visited = [False] * vertices
    
    print(adjList)
    print(visited) 

    # Perform BFS traversal starting from vertex 0
    print("Breadth First Traversal starting from vertex 0:", end=" ")
    bfs(adjList, 0, visited)
    print(adjList)
    print(visited) 

if __name__ == "__main__":
    main()
