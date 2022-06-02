n=int(input())
k=[]
a=list(map(int,input().split()))
for i in a:
    k.append (i**2)
print(*(sorted(k)))
