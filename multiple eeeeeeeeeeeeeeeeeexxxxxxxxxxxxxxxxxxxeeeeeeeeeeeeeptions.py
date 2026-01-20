try:
    num1, num2=eval(input("Enter two numbers seperated by a comma: "))
    result=num1/num2
    print("THE RESULT IS............ ", result)
except ZeroDivisionError:
    print("THIS NUMBER IS NOT DIVISIBLE BY 0!!!!!!!!!!!!!!!!!")
except SyntaxError:
    print("YOU FORGOT TO WRITE A COMMA TRY AGAIN (BUT WITH A COMMA THIS TIME)!!!!!!!!!!!!!!!!")
except:
    print("YOU GAVE ME A WRONG INPUT!!!!!!!!!!!!!!!!!!")
else:
    print("NO EXCEPTIONS AT ALL!!!!!!!!!!!!!!!!!!!!!!!")
