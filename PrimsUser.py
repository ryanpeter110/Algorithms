import time
graph={}
no=int(input("Enter Number Of Nodes: "))
for i in range(no):
  graph[i]={}
  print ("Enter Number Of Nodes Connected to",i)
  n=int(input())
  for j in range(n):
    x,w=map(int,input("Enter Node and Weight\n").split())
    graph[i][x]=w
print (graph)    
def Prims():
  U,V=set([1]),(graph.keys())
  result=[]
  while len(U) != len(V):
    minw=-1
    mine=[]
    for u in U:
      for v in graph[u]:
        if v in V-U:
          if minw==-1 or minw>graph[u][v]:
            minw=graph[u][v]
            mine=[u,v]
    mine.append(minw)
    result.append(mine)
    U.add(mine[1])
  return result
start=time.clock()
print (Prims())
end=time.clock()
print ("Program Ran for: ",end-start,"seconds")
