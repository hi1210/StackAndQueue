from stack import Stack

if __name__ == "__main__":
    stringStrang = input("Enter the string to be reversed: ")
    stringStack = Stack()
    for char in stringStrang:
        stringStack.push(char)
    while stringStack.isEmpty() == False:
        print(stringStack.pop().data, end="")
    print()
