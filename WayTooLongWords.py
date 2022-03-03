#A. Way Too Long Words            


n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
for x in range(len(arr)):
    
    if len(arr[x])>10:
        arr[x]=arr[x][0]+str(len(arr[x])-2)+arr[x][-1]
for x in range(len(arr)):
    print(arr[x])
    
    
    
    
    