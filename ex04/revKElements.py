from stack import Stack
from queue import Queue

if __name__ == "__main__":
    stringStrang = input("Enter the list of numbers: ")
    stringQueue = Queue()
    stringStack = Stack()
    if stringStrang != "":
        for i in stringStrang.split(","):
            stringQueue.enqueue(int(i))
        for i in range(int(input("Enter k: "))):
            if stringQueue.isEmpty():
                break
            stringStack.push(stringQueue.front().data)
            stringQueue.dequeue()
        while stringStack.isEmpty() == False:
            if stringQueue.isEmpty() and stringStack.size() == 1:
                print(stringStack.pop().data)
            else:
                print(stringStack.pop().data, end = ",")
        while stringQueue.isEmpty() == False:
            if stringQueue.size() == 1:
                print(stringQueue.front().data)
            else:
                print(stringQueue.front().data, end = ",")
            stringQueue.dequeue()
