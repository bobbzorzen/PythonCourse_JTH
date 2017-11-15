import json
def store(list_of_values):
    with open("calculator_state.json", "w") as fp:
        json.dump(list_of_values, fp)

def load():
    with open("calculator_state.json", "r") as fp:
        return json.load(fp)
    
def getIntegerInput(inputText, errorMessage="Invalid number"):
    while True :
        try:
            return int(input(inputText))
        except:
            print(errorMessage)

def getOperationInput(inputText, errorMessage="Invalid operation"):
    while True :
        operation = input(inputText)
        if(operation in ["add", "sub", "mul", "div", "quit", "undo", "store", "load"]):
            return operation
        else:
            print(errorMessage)

def calculator():
    memory_value = getIntegerInput("Enter initial  memory value: ")
    undo_list = [memory_value]
    operation = ""
    while operation != "quit":
        operation = getOperationInput("Enter operation (add/sub/mul/div/quit): ")
        if operation == "add":
            secondary_number = getIntegerInput("Enter operand: ")
            memory_value = memory_value + secondary_number
            undo_list.append(memory_value)
        elif operation == "sub":
            secondary_number = getIntegerInput("Enter operand: ")
            memory_value = memory_value - secondary_number
            undo_list.append(memory_value)
        elif operation == "mul":
            secondary_number = getIntegerInput("Enter operand: ")
            memory_value = memory_value * secondary_number
            undo_list.append(memory_value)
        elif operation == "div":
            if secondary_number == 0:
                print("Zero division error, please try again")
            else:
                secondary_number = getIntegerInput("Enter operand: ")
                memory_value = memory_value / secondary_number
                undo_list.append(memory_value)
        elif operation == "undo":
            if len(undo_list) > 1:
                undo_list.pop()
                memory_value = undo_list[-1]
            else:
                print("There is nothing to undo")
        elif operation == "store":
            store(undo_list)
        elif operation == "load":
            undo_list = load()
            memory_value = undo_list[-1]

        print(memory_value, " is stored in memory.")
    return memory_value

print("The program finished with " + str(calculator()) + " in memory.")
