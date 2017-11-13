
def getIntegerInput(inputText, errorMessage="Invalid number"):
    while True :
        try:
            return int(input(inputText))
        except:
            print(errorMessage)

def getOperationInput(inputText, errorMessage="Invalid operation"):
    while True :
        operation = input(inputText)
        if(operation in ["add", "sub", "mul", "div", "quit", "undo"]):
            return operation
        else:
            print(errorMessage)

def calculator():
    undo_list = []
    memory_value = getIntegerInput("Enter initial  memory value: ")
    operation = getOperationInput("Enter operation (add/sub/mul/div/quit): ")
    while operation != "quit":
        if operation != "undo":
            secondary_number = getIntegerInput("Enter operand: ")
            undo_list.append(memory_value)
            if operation == "add":
                memory_value = memory_value + secondary_number
            elif operation == "sub":
                memory_value = memory_value - secondary_number
            elif operation == "mul":
                memory_value = memory_value * secondary_number
            elif operation == "div":
                if secondary_number == 0:
                    print("Zero division error, please try again")
                else:
                    memory_value = memory_value / secondary_number
        else:
            if len(undo_list) > 0:
                memory_value = undo_list.pop()
            else:
                print("There is nothing to undo")
        print(memory_value, " is stored in memory.")
        operation = getOperationInput("Enter operation (add/sub/mul/div/quit): ")
    return memory_value

print("The program finished with " + str(calculator()) + " in memory.")