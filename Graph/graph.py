from collections import defaultdict, deque

class Graph: 
    def __init__(self):
        self.adjList = defaultdict(list)
 
    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.adjList[u].append(v)
        print("Edge added from", u, "to", v)

    def bfs(self, startNode):
        # Create a queue for BFS
        queue = deque()
        visited = [False] * (len(self.adjList)*5)
 
        # Mark the current node as visited and enqueue it
        visited[startNode] = True
        queue.append(startNode)
 
        # Iterate over the queue
        while queue:
            # Dequeue a vertex from queue and print it
            currentNode = queue.popleft()
            print(currentNode, end=" ")
 
            # Get all adjacent vertices of the dequeued vertex currentNode
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for neighbor in self.adjList[currentNode]:
                #print("Current: ", currentNode, "<end current>\n")
                #print("Neighbor: ", neighbor, "<end neighbors>\n")
                if not visited[neighbor]:
                    visited[neighbor] = True
                    #print("Visited node ", neighbor, "<end visit>\n")
                    queue.append(neighbor)

# Create a graph
graph = Graph()
 
# Add edges to the graph
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4)
 
# Perform BFS traversal starting from vertex 0
print("Breadth First Traversal starting from vertex 0:", end=" ")
graph.bfs(0)