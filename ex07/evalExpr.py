from stack import Stack
from queue import Queue

def main():
    stringStrang = input("Enter the function: ")
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
                balanced = False
                break
            if stringStack.peek().data != setDict[char]:
                balanced = False
                break
            else:
                stringStack.pop()
    if stringStack.isEmpty() == False:
        balanced = False
    if balanced:
        stringStrang = stringStrang.replace(" ", "")
        while isOneNum(stringStrang) == False:
            firstEval = 0
            lastEval = len(stringStrang)
            for i in range(len(stringStrang)):
                if stringStrang[i] in openers:
                    firstEval = i
                if stringStrang[i] in closers:
                    lastEval = i
                    break
            if stringStrang[firstEval] in openers:
                stringStrang = stringStrang[0:firstEval] + str(evaluate(stringStrang[firstEval+1:lastEval])) + stringStrang[lastEval+1:len(stringStrang)]
            else:
                stringStrang = str(evaluate(stringStrang[firstEval:lastEval]))
        if(float(stringStrang) == int(float(stringStrang))):
            print(int(float(stringStrang)))
        else:
            print(stringStrang)
    else:
        print("brackets are unbalanced")

def evaluate(theString):
    #print("theString is " + theString)
    funcList = []
    index = 0
    while index < len(theString):
        operatorIndex = index
        while operatorIndex < len(theString) and (isOneNum(theString[operatorIndex]) or theString[operatorIndex] == "."):
            operatorIndex = operatorIndex + 1
        funcList.append(gatherNearNums(theString, index))
        if operatorIndex >= len(theString)-1:
            break
        funcList.append(theString[operatorIndex])
        #print(funcList)
        index = operatorIndex
        index += 1
    i = 0
    while i < len(funcList):
        if funcList[i] == "*" or funcList[i] == "/":
            if funcList[i] == "*":
                funcList.insert(i-1,funcList[i-1] * funcList[i+1])
            if funcList[i] == "/":
                funcList.insert(i-1,funcList[i-1] / funcList[i+1])
            del funcList[i]
            del funcList[i]
            del funcList[i]
        i += 1
    i = 0
    while i < len(funcList):
        if funcList[i] == "+" or funcList[i] == "-":
            if funcList[i] == "+":
                funcList.insert(i-1,funcList[i-1] + funcList[i+1])
            if funcList[i] == "-":
                funcList.insert(i-1,funcList[i-1] - funcList[i+1])
            del funcList[i]
            del funcList[i]
            del funcList[i]
        i += 1
    return funcList[0]

def gatherNearNums(theString, index):
    numString = theString[index]
    baseIndex = index
    index = index-1
    #print("started with: " + str(numString))
    while index >= 0:
        foundNum = False
        if isOneNum(theString[index]) or theString[index] == ".":
            numString = theString[index] + numString
            index = index -1
            #print("numString added: " + str(numString))
            foundNum = True
        if foundNum == False:
            break
    index = baseIndex + 1
    while index < len(theString):
        foundNum = False
        if isOneNum(theString[index]) or theString[index] == ".":
            numString = numString + theString[index]
            #print("numString added: " + str(numString))
            index = index + 1
            foundNum = True
        if foundNum == False:
            break
    return float(numString)

def isOneNum(theString):
    try:
        float(theString)
        return True
    except ValueError as e:
        return False

if __name__ == "__main__":
    main()
