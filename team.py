# team                  

n=int(input())
out=0

for i in range(n):
    p,v,t=map(int,input().split(' '))
    if (p+v+t)>=2:
        out+=1
print(out)