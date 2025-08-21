#break
num=0
for i in range(10):
    num +=1
    if num == 8:
        break
    print("The Number has Value : ", num)
print("Out Of The Loop")


#Continue
num=0
for i in range(10):
    num +=1
    if num ==8:
        continue
    print("The Num Has Valie : ", num)
print("Out of Loop !!")