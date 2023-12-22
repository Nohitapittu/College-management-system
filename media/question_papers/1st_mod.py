'''def add(a,b):
    return a+b'''
def avg(*n):
    s=1
    for i in range(len(n)):
        s=s+i
        print('s',s)
        avg=s/len(n)
        print('avg',avg)
    return avg
