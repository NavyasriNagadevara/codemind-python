x,y=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
s=[]
for i in l:
    if i in m:
        if i not in s:
            s.append(i)
print(*s)