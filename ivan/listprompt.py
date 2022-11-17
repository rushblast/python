x=int(input("Enter the number of strings:"))
print("Enter the elements:")
list=[]
for i in range(0,x):
    ele=int(input())
    if(ele>100):
        list.append('over')
    else:
        list.append(ele)
print(list)