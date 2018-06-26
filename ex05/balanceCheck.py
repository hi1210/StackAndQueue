from stack import Stack
from queue import Queue

if __name__ == "__main__":
    stringStrang = input("Enter the sequence: ")
    stringStack = Stack()
    openers = ["{", "[", "("]
    closers = ["}", "]", ")"]
    setDict = {"}":"{", "]":"[", ")":"("}
    balanced = True
    for char in stringStrang:
        if char in openers:
            stringStack.push(char)
        if char in closers:
            if stringStack.peek() == None:
                print("False")
                balanced = False
                break
            if stringStack.peek().data != setDict[char]:
                print("False")
                balanced = False
                break
            else:
                stringStack.pop()
    if stringStack.isEmpty() == False:
        balanced = False
    if balanced:
        print("True")
