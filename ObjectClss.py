class Calculator:
    def add(self,a,b):
        s=a+b;
        print(f"Sum:{s}")
    def sub(self,a,b):
        d = a-b
        return d
    def mod(self,a,b):
        e = a%b
        print(f"Mod : {e}")
    def flow(self,a,b):
        pass
        
obj = Calculator()
obj.add(4,2)
diff = obj.sub(9,4)
print(f"Difference : {diff}")
obj.mod(4,5)
