from stack import Stack

if __name__ == '__main__':
    stickStack = Stack()
    print(stickStack.isEmpty())
    stickStack.push(2)
    stickStack.push("Hello")
    print(stickStack.__str__())
    print(stickStack.size())
    print(stickStack.peek().data)
    print(stickStack.pop().data)
    print(stickStack.isEmpty())
    stickStack.pop()
    print(stickStack.isEmpty())
    print(stickStack.peek())
    print(stickStack.pop())
