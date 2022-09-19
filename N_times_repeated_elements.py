x=int(input())
l=list(map(int,input().split()))
k=set(l)
y=int(input())
c=0
for i in k:
    if l.count(i)==y:
        c+=1
        print(i,end=" ")
if c==0:
    print("-1")