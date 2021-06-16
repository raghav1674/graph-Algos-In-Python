from utils import Node,Edge 

class Graph:
        
        def __init__(self,num_of_vertices,is_directed=False):
                
                self.num_of_vertices = num_of_vertices
                self.adj_list = [None]*self.num_of_vertices 
                self.is_directed = is_directed
                self.__edge_list = []
                self.__adj_matrix = [list([0]*(self.num_of_vertices+1)) for _ in range(self.num_of_vertices+1)]
                
        def insert(self,src,dest,cost=1):
                
                
                if (src <= self.num_of_vertices and src >0 )and (dest > 0 and dest <= self.num_of_vertices):
                        
                        self.__adj_matrix[src][dest] = cost
                        newEdge = Edge(src,dest,cost)
                        self.__edge_list.append(newEdge)
                        newNode = Node(dest-1)
                        newNode.next = self.adj_list[src-1]
                        self.adj_list[src-1] = newNode
                        if not self.is_directed:
                                self.__adj_matrix[dest][src] = cost
                                
                                
                                newNode = Node(src-1)
                                newNode.next = self.adj_list[dest-1]
                                self.adj_list[dest-1] = newNode 
                else:
                    try:
                        raise Exception("Please Enter the source and destination in the range of (1,{})".format(self.num_of_vertices))
                    except Exception as e:
                        print(e)
        
        def print_graph(self):
            print('\t{')
            
            for index,vertices in enumerate(self.adj_list):
                
                print('\t\t'+str(index+1)+":",end=" ")
                print(vertices)
            print('\t}')  
        
        
        def dfs(self):
            
            print("="*5,end=" ")
            print("DFS",end=" ")
            print("="*5)
            
            components = []
            
            visited = [False]*self.num_of_vertices
            
            for vertex in range(self.num_of_vertices):
                
                if not visited[vertex]:
                    
                    self.__dfs_helper(vertex,visited,components)
                    
            print("\n===== Connected Components ======")
            
            print(components)    
        	 
        def __dfs_helper(self,start,visited,components):
            
            connected = []
            stack = []
            current = start 
            visited[current] = True 
            stack.append(current)
            
            while len(stack) > 0: 
                
                current = stack.pop() 
                
                print(current+1,end=" ")
                
                connected.append(current+1)
                
                if self.adj_list[current] is not None:
                    
                    for neighbour in self.adj_list[current]:
                        
                        if not visited[neighbour]:
                            
                            stack.append(neighbour)
                            
                            visited[neighbour] = True
                            
            components.append(connected)
            
            
        def get_edge_list_repr(self):
             return self.__edge_list
            
        def bfs(self):
            
            print("="*5,end=" ")
            print("BFS",end=" ")
            print("="*5)
            
            visited = [False]*self.num_of_vertices
            
            for vertex in range(self.num_of_vertices):
                
                if not visited[vertex]:
                    
                    self.__bfs__helper(vertex,visited)
                    
                    
        def __bfs__helper(self,start,visited):
            
                 
            queue = []
            current = start
            queue.append(current)
            visited[current] = True 
            
            while len(queue) > 0:
                
                current = queue.pop(0)
                
                print(current+1,end=" ")
                
                if self.adj_list[current] is not None:
                    
                    for neighbour in self.adj_list[current]:
                        
                        if not visited[neighbour]:
                            
                            visited[neighbour] = True
                            
                            queue.append(neighbour)
            
        
        def get_adj_matrix_repr(self):
                return self.__adj_matrix
  
        def __root(self,node,nodeSet):
            while(node != nodeSet[node]):
                node = nodeSet[node] 
            return node 
                
            
        def __find(self,nodeA,nodeB,nodeSet):
            return self.__root(nodeA,nodeSet) == self.__root(nodeB,nodeSet)
            
        def __union(self,nodeA,nodeB,nodeSet):
            nodeSet[self.__root(nodeB,nodeSet)] = self.__root(nodeA,nodeSet) 
            
            
            
        def kruskal_algorithm(self):
            
            nodeSet = [node for node in range(self.num_of_vertices)]
            
            final_set = []
            
            k_edge_list = self.__edge_list.copy()
            
            k_edge_list.sort(key=lambda edge:edge.weight)
            print(k_edge_list)
            for each_edge in k_edge_list:
                
                if not self.__find(each_edge.src-1,each_edge.dest-1,nodeSet):
                    
                    final_set.append(each_edge)        
                    
                    self.__union(each_edge.src-1,each_edge.dest-1,nodeSet)
            
            print(final_set)
                 
             
            

            
