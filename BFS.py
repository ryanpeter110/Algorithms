import time
graph={
        1:[2,3],      
        2:[1,3,4,5],
        3:[1,2,6,7],
        4:[2,5,8,9],
        5:[2,4,9],
        6:[3,7],
        7:[3,6],
        8:[4,9],
        9:[4,5,8,10],
        10:[9]
}
visited=[0,0,0,0,0,0,0,0,0,0]
queue=[]
def bfs(node):
        visited[node-1]=1
        queue.append(node)
        while(queue):
                print queue[0]
                x=queue.pop(0)
                for k in graph[x]:
                        if visited[k-1]==0:
                                queue.append(k)
                                visited[k-1]=1
start=time.clock()
bfs(1)
end=time.clock()
print("The program ran for:")
print(end-start)
print("seconds")
