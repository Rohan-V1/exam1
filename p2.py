str=input("Enter the string: ")
d={}
print("String: ",str)
for i in str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print("Frequency: ",d)  

