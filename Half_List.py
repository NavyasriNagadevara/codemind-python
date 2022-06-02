n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a[n:(n//2)-1:-1]:
    k.append (i)
for j in a[0:n//2]:
    k.append(j)
print(*k)
    
    