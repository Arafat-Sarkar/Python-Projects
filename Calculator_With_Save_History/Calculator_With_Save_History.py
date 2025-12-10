HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE , 'r')
    lines = file.readlines()
    if len(lines)==0:
        print("No histroy found!")

    else:
        for line in reversed(lines):
            print(line.strip())

    file.close()

def clear_histroy():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History Cleared.")


def save_to_history(equation, result):
    file = open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result)+ "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()

    if len(parts)!=3:
        print("Invalid Input. Use format: number operator")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2
    
    elif op == "/":
        if num2 == 0:
            print("Cannot Divide by zero")
        result = num1 / num2

    else:
        print("Invalid Operator. Use Operator + - * /")
        return
    
    if int(result) == result:
        result = int(result)
    print("Result:", result)

    save_to_history(user_input , result)
    
def main():
    print("--SIMPLE CALCULATOR (Type history, clear or exit)")

    while True:
        user_input = input("Enter The Calculation( + - * /) or Command (history clear or exit) = ")
        if user_input == 'exit':
            print("Goodbye")
            break
        elif user_input == 'history':
            show_history()

        elif user_input == 'clear':
            clear_histroy()
        else:
            calculate(user_input)

main()