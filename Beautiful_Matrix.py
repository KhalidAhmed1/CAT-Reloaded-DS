#A. Beautiful Matrix   

a=0
arr=[]
for i in range(5):
        arr.append(list(map(int,input().split(' '))))

for i in range(5):
    if 1 in arr[i]:
        arr[i],arr[2]=arr[2],arr[i]
        a=abs(2-i)
        for j in range(5):
            if arr[2][j]==1:
                arr[2][j],arr[2][2]=0,1;
                a+=abs(2-j)                 
        break
print(a)
