class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if(a == 0 or b == 0): return 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        if a == 0 :
            return 0
        if b == 0:
            return "B can't be 0"
        
        if(a>0 and b>0):
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
        
        elif (a>0 and b<0):
            while a >= b:
                a = self.add(a, b)
                result -= 1
            return result+2
        
        elif (a<0 and b>0):
            while a <= b:
                a = self.add(a, b)
                result -= 1
            return result+2

        elif (a<0 and b<0):
            while a <= b:
                a = self.subtract(a, b)
                result += 1
            return result
    
    def modulo(self, a, b):
        if(b==0):
            return "b can't be 0"
        
        if (a > 0 and b < 0 ):
            while(1):
                a += b
                if(a <= 0):
                    return a
        
        elif (a < 0 and b > 0):
            while(1):
                a += b
                if(a >= 0):
                    return a
                
        elif (a < 0 and b < 0):
            while(a <= b):
                a -= b
            return a
        else:
            while a >= b:
                a -= b
            return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(22, -5))
    print("Example: modulo: ", calc.modulo(9, -4))