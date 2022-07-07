def freq(path):
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
            c=c+1
            d[i]=d[i]+1
    print(d)
freq("/home/administrator/nidhin/python/day2/sample.txt")
