price = 2650
paid = 10000

num_bills = [0,0,0,0,0] #5000,1000,500,100,50

change = paid-price

li = [5000,1000,500,100,50]
for i in li:
    while change >= i:
        num_bills[li.index(i)] += 1
        change -= i
for j in num_bills:
    print(j)
