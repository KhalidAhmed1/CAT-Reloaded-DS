#A. Next Round              

n,k=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
coun=0   

if (1<=k) and (k<=n) and (n<=50):
    for i in range(len(arr)):
            if arr[i] >= arr[k-1] and arr[i]>0:
                coun+=1
    print(coun)
    
    
    
    
    
    
    