from graph import Graph 


if __name__ == "__main__":
	mygraph = Graph(6)
	mygraph.insert(1,2,10)
	mygraph.insert(1,4,9)
	mygraph.insert(2,3,30)
	mygraph.insert(3,5,1),
	mygraph.insert(6,1,7)
	mygraph.insert(6,5,2)
	# mygraph.insert(2,7)
	mygraph.insert(3,1,12)
	mygraph.print_graph()
	mygraph.dfs()
	mygraph.bfs()
	print("\n==== Edge List Repr ====")
	print(mygraph.get_edge_list_repr())

	print("=== Adj Matrix Repr ====")
	adj_matrix = mygraph.get_adj_matrix_repr()
	for vertices in adj_matrix[1:]:
		print(vertices[1:])
  
	mygraph.kruskal_algorithm()
		
		
		
                
                
                
                
                