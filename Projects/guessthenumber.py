import random
randnum = random.randint(1,100)
while True :
    try :
        asknum = int(input("Guess between 1 to 100 :"))
        if asknum > randnum:
            print ('Too High !')
        elif asknum < randnum:
            print('Too Low')
        else:
            print('Congratulations You Guessed the Number.') 
            break
    except ValueError:
        print('please Enter a Valid Number')

