#A. Bit++            

n=int(input())
arr=[]
res=0
if (1<=n) and (n<=150):
    for i in range(n):
        arr.append(input())
    for x in range(len(arr)):
        if arr[x]=='++X' or arr[x]=='X++'or arr[x]=='++x' or arr[x]=='x++':
            res+=1
        elif arr[x]=='--X' or arr[x]=='X--'or arr[x]=='--X' or arr[x]=='X--': 
            res-=1
    print(res)