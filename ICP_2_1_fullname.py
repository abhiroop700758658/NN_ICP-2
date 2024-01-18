def fullname(fname, lname):
    funame=fname+" "+lname
    return (funame)

def string_alternative(funame):
    st=""
    for i in range(len(funame)):
        if(i%2==0):
            st=st+funame[i]
    return st

fname=input("enter your first name:\n")
lname=input("enter your last name:\n")
funame=fullname(fname,lname)
print(funame)
print(string_alternative(funame))
