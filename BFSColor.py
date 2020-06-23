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
layer=[]
color=[""]*20
def bfs(node):
        i=0
        visited=[0]*11
        visited[node]=1
        color[i]="red"
        layer.append([node])
        print node
        while len(layer[i])!=0:
                r=[]
                for k in layer[i]:
                        for j in graph[k]:
                                if visited[j]==0:
                                        print j
                                        visited[j]=1
                                        r.append(j)
                                        if (i+1)%2==0:
                                                color[i+1]="red"
                                        else:
                                                color[i+1]="blue"
                layer.append(r)
                i+=1
        print color[:i]
bfs(1)
