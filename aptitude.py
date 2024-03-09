
l = int(input("enter a number of line"))

for i in range(1,l+1):
    for j in range(1,i+1):
        print(j,end =" ")
    
    for j in range(1,l*2-i*2+1):
        print(" ",end =" ")
    for j in range(1,i+1):
        print(i-j+1,end =" ")
    print()   


        
    



 

