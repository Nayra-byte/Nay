import random
playing = True 
number=int(random.randint(10,20))
print("I will generate a number between 0 - 9 and you have to guess it 🤨🤨")
print("The game ends whe you get 1️⃣ point")
while playing:
    guess = input("Give me your best guess!!\n")
    if number==guess:
        print("🫵🏻🏆😜")
        print("The number is.............",number)
        break
    else:
        print("🫵🏻😭😭😭")
        print("try again")
