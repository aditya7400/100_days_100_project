import art , os
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
operations_save = ("""+
-
*
/
:""")
exit_program = False
output = 0
n = 0
while not exit_program:
    if n == 0:
        num1 = int(input("Enter first number: "))
        operator = input(operations_save)
        num2 = int(input("Enter second number: "))
        output = operations[operator](num1,num2)
        result = f"{num1} {operator} {num2} = {output}"
        print(result)
    ask = input("want to continue with this result[type y] or start a new calculation[type n]")
    if ask == 'y':
        operator = input(operations_save)
        num2 = int(input("Enter Second number: "))
        num1 = output
        output = operations[operator](output,num2)
        result = f"{num1} {operator} {num2} = {output}"
        print(result)
        n =1
    else:
        os.system('cls')
        print(art.logo)
        n = 0