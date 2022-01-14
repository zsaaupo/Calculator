"""
Calculator
"""
print(__doc__)

class calculator():
    """
    Calculator methods
    """

    def sum(self, a, b):
        return a + b

    
    def sub(self, a, b):
        return a - b

    
    def mult(self, a, b):
        return a * b


    def div(self, a, b):
        return a / b


    def fdiv(self, a, b):
        return a // b


    def rdiv(self, a, b):
        return a % b

    
    def square(self, a, b):
        return a * a , b * b


    def cube(self, a, b):
        return a * a * a , b * b * b


    def hsquare(self, a, b):
        return (a + b) * (a + b)


    def msquare(self, a, b):
        return (a - b) * (a - b)


operation = calculator()


i = 1


while i == 1:
    

    e = 1


    while e == 1:
      
       
        print("Enter your oparetion, for Summation write 'sum', for Subtraction write 'sub',for Multiplication write 'mult' for Divition write 'div',\nfor floor division write 'fdiv', for divition remainder writ 'rdiv', for square of 2 separate value write 'square', for cube of 2 separate value write 'cube', \nfor a + b whole square of 2 values write'hsquare', for a - b whole square of 2 values write'msquare'")
        s = input()
        

        print("Enter frist value")
        a = int(input())
        

        print("Enter second value")
        b = int(input())
        

        if s == "sum":
            print("Summation of your value = ", operation.sum(a, b), "\n")
            

        if s == "sub":
            print("Subtraction of your value = ", operation.sub(a, b), "\n")


        if s == "mult":
            print("Multiplication of your value = ", operation.mult(a, b), "\n")


        try:
            if s == "div":
                print("Divition of your value = ", operation.div(a, b), "\n")
        except ZeroDivisionError:
            print("you can't divie a value with '0'")
        

        if s == "fdiv":
            print("floor division of your value = ", operation.fdiv(a, b), "\n")


        if s == "rdiv":
            print("divition remainder of your value = ", operation.rdiv(a, b), "\n")


        if s == "square":
            print("square of 2 values are in sequence 1st value and 2nd value =", operation.square(a, b), "\n")


        if s == "cube":
            print("cube of 2 values are in sequence 1st value and 2nd value =", operation.cube(a, b), "\n")


        if s == "hsquare":
            print("a + b whole square of 2 values are =", operation.hsquare(a, b), "\n")


        if s == "msquare":
            print("a - b whole square of 2 values are =", operation.msquare(a, b), "\n")
        

        if s == "exit":
            e = 2
        print("if you want to close the program write 'exit' and give 2 randon value or continue\n")

        
    else:
        break