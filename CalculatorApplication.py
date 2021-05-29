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



operation = calculator()

i = 1

while i == 1:
    
    e = 1

    while e == 1:
        
        print("Enter your oparetion, for Summation write 'sum', for Subtraction write 'sub',for Multiplication write 'mult' for Divition write 'div'")
        s = input()
        
        print("Enter frist value")
        a = int(input())
        
        print("Enter second value")
        b = int(input())
        
        if s == "sum":
            print("Summation of your value = ", operation.sum(a, b))
            

        if s == "sub":
            print("Subtraction of your value = ", operation.sub(a, b))

        if s == "mult":
            print("Multiplication of your value = ", operation.mult(a, b))

        try:
            if s == "div":
                print("Divition of your value = ", operation.div(a, b))
        except ZeroDivisionError:
            print("you can't divie a value with '0'")
        
        if s == "exit":
            e = 2
        print("if you want to close the program write 'exit' and give 2 randon value or continue")
    else:
        break