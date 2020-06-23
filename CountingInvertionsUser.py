import time
def merge(a,b):
        m,c = [],0
        if a[0] <= b[0]:
                m.append(a.pop(0))
        else:
                c += len(a)
                m.append(b.pop(0))
        m += a
        m += b
        return m,c
def sort(arr):
        if len(arr) <= 1:
                return arr,0
        mid = len(arr)//2
        b,r1 = sort(arr[:mid])
        c,r2 = sort(arr[mid:])
        d,c = merge(b,c)
        return d,(r1+r2+c)
y = []; x = [];
n=int(input("Enter range of numbers : "))
for i in range(n):
    num=int(input("Enter value"))
    x.insert(i,num);y.insert(i,num);
start= time.clock()
s,c = sort(x)
end= time.clock()
print "Initial list: ",x
y.sort()
print "Sorted list: ",y
print "Number of Invertions: ",c
print "Time :",end-start
