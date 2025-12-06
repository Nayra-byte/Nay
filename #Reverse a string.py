string=str(input("Enter the string you want to reverse: "))
str2=('')
for i in string:
    str2=i+str2
print("Original string: ",string)
print("Reverse string: ",str2)