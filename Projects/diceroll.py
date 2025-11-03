import random

while True:
    ans = input('Roll the Dice ? (y/n)').lower()
    if ans=='y':
        print("Dice Rolled !")
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print(f'Your Number is : ({num1}, {num2})')
    
    elif ans=='n':
        print('Thanks for Playing')
        break
    else:
        print('Invalid choice !')
    