def freq():
    path="/home/administrator/nidhin/python/day2/sample.txt"
    s=open(path).read()
    print(s)
    h=s.split()
    count=0
    d={}
    for i in h:
        if len(i)%2!=0:
            if i not in d:
                count=1
                d[i]=count
            else:
                d[i]=d[i]+1
    print(d)
