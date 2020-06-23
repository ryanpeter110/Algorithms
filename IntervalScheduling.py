import time
def printMaxActivities(s,f):
    n = len(f)
    print ("The following activities are selected")
    i = 0
    print (i)
    for j in range(n):
        if s[j] >= f[i]:
            print (j)
            i = j
s = []
no=int(input("Enter size: "))
for u in range(no):
        s.insert(u,int(input("Enter Values:")))
print(s)
f = []
no1=int(input("Enter size: "))
for v in range(no1):
        f.insert(v,int(input("Enter Values: ")))
print(f)
start=time.clock()
printMaxActivities(s,f)
end=time.clock()
print("The program ran for: ",end-start,"seconds")
