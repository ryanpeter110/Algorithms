import time
graph={
    1:{ 2:10, 5:100},
    2:{ 1:10, 3:50},
    3:{ 2:50, 4:20, 5:10},
    4:{ 3:20, 5:60},
    5:{ 1:100, 3:10, 4:60}
}
def Dijkstra(s):
	d,visited=[float('inf')]*len(graph),[0]*len(graph)
	d[s-1]=0
	visited[s-1]=1
	vertices=[s]
	print "\nStart --> ",
	print s," --> ", #printing start node
	path={} #dictionary to hold the weight as key and the edge traversed as value
	while len(vertices)!=len(graph):
		edge={}
		for u in vertices:
			for v in graph[u]:
				if visited[v-1]==0:
					t=d[u-1]+graph[u][v]
					edge.update({t:[u,v]})
		min_d=min(edge.keys())
		node=edge[min_d][1]
		print node," --> ", #printing the node in which it is traversed
		d[node-1]=min_d
		visited[node-1]=1
		vertices.append(node)
		path.update({min_d:[edge[min_d][0],node]}) #update edge being traversed with the current weight
	print " Destination "
	print "\n","Weight | Path","\n"
	for i in sorted(path.keys()):
		print "{",i,":",path[i],"}" #printing the dictionary with the weights and path traversed
	print "\nWeights taken in the given path using Greedy Algorithm : \n" 
	return d
start=time.clock()
print Dijkstra(1)
end=time.clock()
print "The Program Ran for: ",end-start,"seconds"
