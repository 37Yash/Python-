n=30
list=[]
for i in range(1,n):
    count=0
    for j in range(1,30):
        if(i%j==0):
            count=count+1
            
    if(count==2):
        print(i)
        list.append(i)


print(list)
print("Reverse of a list : ")
list.reverse()
print(list)



   
   
