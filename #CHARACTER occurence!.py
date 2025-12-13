n=str(input("Please enter a word: "))
l=str(input("Please enter a character: "))
i=0
p=0
while(i<len(n)):
    if(n[i]==l):
        p=p+1
    i=i+1
print("\nThe amount of times ", l, " has occured is ", p)