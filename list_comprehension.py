#list comprehension 
if __name__ == '__main__':
    x=int(input("x:"))
    y=int(input("y:"))
    z=int(input("z:"))
    n=int(input("n:"))
    lis=[]    
    for i in range (x+1):          
      for j in range (y+1):              
          for k in range (z+1):
                if i+j+k!=n:
                    lis.append([i,j,k])
     
    print(lis)