def equal(c,d):
    print("Strings are: "+c,d)
    e=0
    if(len(c)!=len(d)):
        return False
    else:
        for i in range(len(c)):
            if(c[i]!=d[i]):
                e+=1
        if(e>1):
            return False
        else:
            return True

a=input("enter the first string: ")
b=input("enter the second string: ")
print(equal(a,b))
