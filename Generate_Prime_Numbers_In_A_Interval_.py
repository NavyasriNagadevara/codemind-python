def prime(n):
    c=0
    for i in range(1,int(pow(n*n,0.5)+1)):
        if n%i==0:
            c+=1
    if c==2:
        print(n)
n=int(input())
r=int(input())
for i in range(n,r+1):
    prime(n)
    n=n+1