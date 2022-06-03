x=int(input())
temp=x
i=x
y=x
while True:
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
             break
    else:
        g=i
        break
    i+=1
while True:
    for j in range(2,int(i**0.5)+1):
        if y%j==0:
            break
    else:
        h=y
        break
    y=y-1
s=abs(temp-g)
k=abs(temp-h)
if s>=k:
    print(k)
else:
    print(s)
        
                