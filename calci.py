from logos import logo
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
def calculator():
    print(logo)
    should_accumulate = True
    num1=float(input("What is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation: ")
        num2=float(input("What is the second number?: "))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice=input("Type 'y' to continue with {answer}, or type 'n' to start again")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()