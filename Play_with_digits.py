n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    st=str(i)
    for j in st:
        s+=int(j)
print(s,end=' ')