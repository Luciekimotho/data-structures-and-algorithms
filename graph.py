class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V     #Initiating an array of lists

    def add_edge(self, src, dest):
        node = AdjNode(dest)              #Add the node to the source node 
        node.next = self.graph[src]
        self.graph[src] = node 

        node = AdjNode(src)               #Add the node to the destination
        node.next = self.graph[dest]
        self.graph[dest] = node 


    def print_graph(self):
        for i in range(self.V):            #Loop through the number of vertices
            print('Vertex {}'.format(i))
            print('Head ', end="")
            temp = self.graph[i]
            while temp:                   #Loop through the nodes in a vertex list
                print('- > {}'.format(temp.vertex), end=" ")
                temp = temp.next
            print(' \n')


V = 5
graph = Graph(V) 
graph.add_edge(0, 1) 
graph.add_edge(0, 4) 
graph.add_edge(1, 2) 
graph.add_edge(1, 3) 
graph.add_edge(1, 4) 
graph.add_edge(2, 3) 
graph.add_edge(3, 4) 

graph.print_graph() 