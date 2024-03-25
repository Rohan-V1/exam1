n=int(input("Enter the number of elemeent"))
a=[]
for i in range(n):
    n=int(input("enter the elements"))
    a.append(n)
l=set(a)    
print("Original list= ",a)    
print("Unique List= ",l)
s=[]
for i in l:
    if a.count(i)==1:
        s.append(i)
print("Single elements are: ",s)

        