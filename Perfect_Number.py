a=int(input())
temp=a
c=0
for i in range(1,a):
    if a%i==0:
        c=c+i
if temp==c:
    print("True")
else:
    print("False")