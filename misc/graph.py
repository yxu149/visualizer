from collections import defaultdict, deque

class Graph: 
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.current_nodes = None
        self.output = []
        self.paths = 0
        self.visited = []
 
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        print("Edge added from", u, "to", v)
        self.paths += 1
        self.visited = [False] * (self.paths + 1)
        print("Paths count:", self.paths)
        

    def bfs(self, startNode):
        # Create a queue for BFS
        queue = deque()
        #visited = [0]
        print("Visited list created with length", len(self.visited))
 
        # Mark the current node as visited and enqueue it
        self.visited[startNode] = True
        queue.append(startNode)
 
        # Iterate over the queue
        while queue:
            # Dequeue a vertex from queue and print it
            current_node = queue.popleft()
            self.output.append(current_node)
            #print(current_node, end=" ")
 
            # Get all adjacent vertices of the dequeued vertex currentNode
            # If an adjacent has not been visited, then mark it visited and enqueue it
            for neighbor in self.adj_list[current_node]:
                print("Current:", current_node, "Neighbor:", neighbor)
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    print("Visited node:", neighbor)
                    queue.append(neighbor)
                else: 
                    print("Node already visited @", neighbor)

# Create a graph
graph = Graph()
 
# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 7)
graph.add_edge(3, 8)
graph.add_edge(2, 9)
graph.add_edge(9, 10)   
graph.add_edge(1, 3)
graph.add_edge(1, 2)
 
# Perform BFS traversal starting from vertex 0
#print("Breadth First Traversal starting from vertex 0:\n", end=" ")
graph.bfs(0)
print("Found path:", graph.output)