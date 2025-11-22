actual_amount= float(input("Enter the actual amount of the product "))
sale_amount= float(input("Enter the sale amount of the product "))
if (sale_amount>actual_amount):
    amount=sale_amount - actual_amount
    print("total profit = {0}".format(amount))
else:
    print ("No profit ＞︿＜.·´¯`(>▂<)´¯`·. ")