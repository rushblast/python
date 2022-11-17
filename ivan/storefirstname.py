num=int(input("Enter the value:"))
n1=0
n2=1
print("Fibanocci series:",n1,"\n",n2)
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
