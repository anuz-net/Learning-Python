a=int(input("Enter Mathi Ko Value : "))
b=int(input("Enter Tala ko Value : "))
try:
    r=a/b
    print("Result is :", r)
except:
    print("Division by zero is Not Possible")
finally:
    print("This is the Final Code That SHould be run at any cost")