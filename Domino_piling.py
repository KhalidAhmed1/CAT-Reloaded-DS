#A. Domino piling            

m,n=map(int,input().split(' '))
total=m*n
if (1<=m)and(m<=n)and(n<=16):
    print(total//2)