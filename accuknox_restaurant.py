import collections

# here in sample1, (1,10) 1 being the eater_id, and 10 being foodmenu_id 
# sample1 is for error case where (6,10) appears twice, whereas sample2 is perfectly ideal case
sample1 = [(1,10),(2,20),(3,30),(4,10),(6,10),(7,20),(6,10)]
sample2 = [(4,18), (1,67),(5,90),(5,18),(1,67),(2,99)]


x = 0
while (x< len(sample1)):
    if sample1.count(sample1[x])>1:
        print('Repetating Pair of Menu ID and Customer ID')
        x = len(sample1)
    else:
        x+=1
      
print(collections.Counter(x[1] for x in sample1)) 

