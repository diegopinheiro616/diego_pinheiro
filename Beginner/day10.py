"""
Day 10 - Functions with Outputs
"""
"""
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("angELa", "yU")
print(formated_string)

def format_name(f_name, l_name):     # <---- Nesse caso com input fora
    # if f_name =='' or l_name == '':
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input('What is your name?'), input('What is your last name?')))

def format_name(f_name, l_name):     # <---- Com MULTIPLUS INPUTs
    if f_name =='' or l_name == '':
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input('What is your name?'), input('What is your last name?')))
"""
# ################ Exercise 1 ####################
# Days in Month - Eu
"""
leap_year = ''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(chosen_year, chosen_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(chosen_year):
        final_month = month_days[chosen_month -1]
        if chosen_month == 2:
            return 29
        else:
            return final_month
    else:
        final_month = month_days[chosen_month - 1]
        return final_month

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
"""
# ################ Exercise 1 ####################
# Days in Month - Dr. Angela Yu
"""
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month entered."
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]


# Do NOT change any of the code below 👇
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
"""
# Doctrings
"""
# Already used functions with outputs.
lengh = len(formatted_name)

# Return as an early exit.
def format_name(f_name, l_name):
    if f_name =='' or l_name == '':
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

format_name()  # <---- O texto escrito dentro das " ""x"" " aparece quando passamos o cursor em cima. Deletei!!!
"""
# ################ Quiz ####################
"""
Question 1: Without running the code below, what do you think will be printed in the console?

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(add(2, multiply(5, divide(8, 4))))

Answer: 12.0 <---- Float

Question 2:
What would you predict to be the result of running the following code?

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

Answer: 15  <---- pois os itens a e b viram outputs c e d

Question 3:
What will be printed in the console after running the following code?

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

Answer: none <---- The return keyword will exit the function and prevent the rest of the code from being executed.
"""
# ################ Exercise 2 ####################
# Calculator - Opção 1 - Diego
"""
from day9_1 import logo2

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def new_calculation():
    print(logo2)
    num1 = float(input('What\'s the first number?: '))

    for symbol in operations:
        print(symbol)
    operation_symbol = input('Pick an operation from the line above: ')
    while operation_symbol not in operations:
        operation_symbol = input('Wrong input. Pick an operation from the line above: ')

    num2 = float(input('What\'s the second number? '))

    if operation_symbol == '+':
        answer = add(num1, num2)
    elif operation_symbol == '-':
        answer = subtract(num1, num2)
    elif operation_symbol == '*':
        answer = multiply(num1, num2)
    elif operation_symbol == '/':
        answer = divide(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')
    old_answer = answer

    continuar_operacao = True

    while continuar_operacao:
        continuar = input(f'Type \'y\' to continue calculating with {answer}, or type \'n\' to do another calculation.: ')
        if continuar == 'n':
            continuar_operacao = False
            new_calculation()
        elif continuar == 'y':
            continuar_operacao = True
            operation_symbol = input('Pick an operation: ')
            num = float(input('What\'s the next number?: '))
            if operation_symbol == '+':
                answer = add(old_answer, num)
            elif operation_symbol == '-':
                answer = subtract(old_answer, num)
            elif operation_symbol == '*':
                answer = multiply(old_answer, num)
            elif operation_symbol == '/':
                answer = divide(old_answer, num)

            print(f'{old_answer} {operation_symbol} {num} = {answer}')
            old_answer = answer

new_calculation()

"""
# ################ Exercise 2 ####################
# Calculator - Opção 2 - Dr. Angela
"""
from day9_1 import logo2

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo2)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
"""