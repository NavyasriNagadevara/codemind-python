x=int(input())
l=list(map(int,input().split()))
s=[]
k=0
for i in l:
    if l.count(i)==i:
        if i not in s:
            s.append(i)
if len(s)==0:
    print("-1")
else:
    print(*s)
        