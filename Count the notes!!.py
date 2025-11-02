amount=int(input("How much money do you want to Withdraw?"))
#variables
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
#printing
print("the notes of 100 rupee are:",note1)
print("the notes of 50 rupee are:",note2)
print("the notes of 10 rupee are:",note3)
