import time
menpref={"V":["C","B","A"],"W":["A","C","B"],"X":["B","A","C"]}
womenpref={"A":["W","X","V"],"B":["X","V","W"],"C":["V","W","X"]}
freemen=["V","W","X"]
takenwomen=[]
final={}
while freemen!=[]:
    for i in freemen:
        listofw=menpref.get(i)
        for j in listofw:
            if j not in takenwomen:
                final[j]=i
                freemen.remove(i)
                takenwomen.append(j)
                break
            else:
                listofm=womenpref.get(j)
                r=final.get(j)
                p=listofm.index(i)
                q=listofm.index(r)
                if p<q:
                    final[j]=i
                    freemen.remove(i)
                    freemen.append(r)
                    takenwomen.append(j)
                    break
print(final)
print("The program ran for:")
print(time.clock())
print("seconds")
