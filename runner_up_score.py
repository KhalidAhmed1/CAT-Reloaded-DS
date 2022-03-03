#runner up score
n = int(input())
if ((2<=n) and (n<=10)):
    arr=map(int,input().split())
    new=sorted(list(set(arr)))
    if(new[0]>=-100 and new[-1]<=100):
        print(list(new)[-2])
        
        
        
        
        