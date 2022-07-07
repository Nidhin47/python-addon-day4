def dicti(path):
    s=open(path).read()
    print(s)
    h=s.split()
    c=0
    d={}
    for i in h:
        if i not in d:
            c=1
            d[i]=c
        else:
            d[i]=d[i]+1
            c=c+1
            return(d)
def second(f):
    e=dicti(f)
    print(e)
second("/home/administrator/nidhin/python/day2/sample.txt")