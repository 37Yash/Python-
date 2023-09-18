cp=int(input("Enter the Cost price of bike : "))
if(cp>100000):
    tax=cp*15/100
    print("Tax is 15% that is : ",tax)
elif (cp>50000 and cp<=100000):
    tax=cp*10/100
    print("Tax is 10% that is : ",tax)
elif (cp<=50000):
    tax=cp*5/100
    print("Tax is 5% that is : ",tax)
