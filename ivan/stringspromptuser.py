l=[]
count=0
n=int(input("Enter the number of strings:"))
print("Enter the names:")
for i in range(0,n):
    string=input()
    l.append(string)
print(l)
for i in l:
    for j in i:
         if j=='a':
              count=count+1
print(count)



