import time
intervals=[[0, 3, 2],[1,4,4],[3,5,4],[2,6,7],[5,7,2]]

intervals.sort(key=lambda x:x[1])


p=[0]*6

def find_p():
	for i in range(len(intervals)-1,-1,-1):
		start_time=intervals[i][0]
		for j in range(i-1,-1,-1):
			end_time=intervals[j][1]
			if end_time<=start_time:
				p[i+1]=j+1
				break
find_p()

m=[-1]*6
m[0]=0

def opt():
	for i in range(1,len(intervals)+1):
		v=intervals[i-1][2]
		m[i]=max(v+m[p[i]],m[i-1])

opt()

final_set=[]

profit=0

def solution():
	j=len(intervals)
	profit=0
	while j!=0:
		if m[j]>m[j-1]:
			final_set.append(j)
			profit+=intervals[j-1][2]
			j=p[j]
		else:
			j=j-1
	return profit
start=time.clock()
print solution()
print final_set
end=time.clock()
print "The Program ran for: ",end-start,"seconds"
