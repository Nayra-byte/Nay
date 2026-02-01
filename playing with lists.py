L=[1,2,657,547,134,67,67,35,98,764,5465756756767]
print("The original list is...................",L)
count=0
for i in L:
    count=+1
avg=count/len(L)
print("Sum=",count)
print("average =", avg)
L.sort()
print("The smallest element is:",L[0])
print("The largest element is:", L[-1])
