import time
def Knapsack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
print("Enter Number Of Items")
n=int(input())
val=[]
for i in range(n):
    val.insert(i,int(input("Enter Values")))
wt=[]
for j in range(n):
    wt.insert(j,int(input("Enter Weights")))
print("Enter Max Weight denoted by W")
W=int(input())
print(val)
print(wt)
print("Max Weight is:",W)
start=time.clock()
print("Final Value in Table is: ",Knapsack(W, wt, val, n))
end=time.clock()
print("The Program ran for: ",end-start,"seconds")
