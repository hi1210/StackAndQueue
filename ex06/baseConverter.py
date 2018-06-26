from stack import Stack
from queue import Queue

if __name__ == "__main__":
    noProblem = True
    baseNum = input("Enter the decimal number: ")
    try:
        baseNum = int(baseNum)
    except ValueError as e:
        print("that is not a decimal integer")
        noProblem = False
    if noProblem:
        baseConv = input("Enter the base: ")
        try:
            baseConv = int(baseConv)
        except ValueError as e:
            print("that is not an integer")
            noProblem = False
        if noProblem:
            placeStack = Stack()
            post9Dict = {10:"A", 11: "B", 12: "C", 13:"D", 14:"E", 15:"F"}
            while baseNum >= baseConv:
                placeStack.push(baseNum % baseConv)
                baseNum = baseNum // baseConv
            if baseNum != 0:
                placeStack.push(baseNum)
            while placeStack.isEmpty() == False:
                digit = placeStack.pop().data
                if digit in post9Dict:
                    digit = post9Dict[digit]
                print(digit, end = "")
            print()
