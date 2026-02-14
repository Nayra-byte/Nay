import array as n
array_num=n.array('i',[1,3,5,3,7,9,3])
print('Original array:'+str(array_num))
print('Number of occurrences of the number 3 in the array are '+str(array_num.count(3)))
array_num.reverse()
print('Reverse order of the items')
print(str(array_num))
