x=input()
k=x.split()
k.sort()
r=sorted(k,key=len)
print(*r)
    
