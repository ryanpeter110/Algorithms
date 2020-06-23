import time
graph=[[1,2,4],[2,3,3],[2,4,1],[1,4,8],[4,3,7],[3,5,8],[4,5,3]]
graph.sort(key=lambda x:x[2])

parent=[-1]*7

def find(i):
	if parent[i]==-1:
		return i
	else:
		return find(parent[i])

def union(i,j):
	i_s=find(i)
	j_s=find(j)
	parent[i_s]=j_s


result=[]

for k in range(0,len(graph)-1):
	u=graph[k][0]
	v=graph[k][1]
	u_s=find(u)
	v_s=find(v)
	if u_s != v_s:
		result.append([u,v,graph[k][2]])
		union(u,v)
start=time.clock()
print result
end=time.clock()
print "The Program ran for: ",end-start,"seconds"
