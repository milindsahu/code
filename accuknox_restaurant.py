import collections

a = [(1,10),(2,20),(3,30),(4,10),(6,10),(7,20),(6,10) ]

print(collections.Counter(x[1] for x in a)) 

x = 0
while (x< len(a)):
    if a.count(a[x])>1:
        print('Repetating Pair of Menu ID and Customer ID')
        x = len(a)
    else:
        x+=1
