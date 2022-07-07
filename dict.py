s=raw_input("enter a string:")
c=0
d={}
for i in s:
    if i not in d:
        c=1
        d[i]=c
    else:
        d[i]=d[i]+1
        c=c+1
print(d)