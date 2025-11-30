mc=(input("Do you have a medical cause Y or N: "))
atten=int(input("Enter the attendance: "))
if (mc=='Y'):
    print("You are allowed, you may proceed")
else:
    if(atten>=75):
        print("You are allowed, you may proceed")
    else:
        print("You are not allowed")
