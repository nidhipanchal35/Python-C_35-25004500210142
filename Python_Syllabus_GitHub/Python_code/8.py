l1=[34, 67, 89, 45, 58]
x=int(input("Enter Value"))
i=0
flag=0
while i<len(l1):
    if(x==l1[i]):
        flag=1
        break
    i=i+1
if(flag==1):
    print("found")
else:
    print("not found")