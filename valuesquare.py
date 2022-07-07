def valsq(x):
    y=range(1,x+1)
    d={}
    for i in y:
        if i not in d:
            d[i]=i*i
    return(d)
def sec(a):
    b=valsq(a)
    print(b)
sec(input("enter a number:"))