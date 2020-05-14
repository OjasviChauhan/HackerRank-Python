Nlist = []
for i in range(int(input())):
    name = input()
    score = float(input())
    List = [name, score]
    Nlist.append(List)
Nlist.sort(key = lambda x: x[1]) 
L = []
for i in range(1,len(Nlist)):
    if Nlist[i][1] > Nlist[0][1]:
        k = i
        break
L.append(Nlist[k][0])
for j in range(k+1,len(Nlist)):
    if Nlist[j][1] == Nlist[j-1][1]:
        L.append(Nlist[j][0])
    else:
        break     
L.sort()
for i in range(len(L)):
    print(L[i])
