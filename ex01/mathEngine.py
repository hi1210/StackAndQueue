from stack import Stack

class Math:
    def runMath(self):
        data = input("Enter the numbers: ").split(", ")
        self.mathStack = Stack()
        self.saveStack = Stack()
        for i in data:
            self.mathStack.push(int(i))
        print(self.mathStack.peek().data)
        print("Total Count = " + str(self.totalCount()))
        print("Sum = " + str(self.sum()))
        self.printProduct()
        self.printMean()
        self.printMin()
        self.printMax()

    def totalCount(self):
        return(self.mathStack.size())

    def sum(self):
        totalSum = 0
        while self.mathStack.isEmpty() == False:
            totalSum = totalSum + self.mathStack.peek().data
            self.saveStack.push(self.mathStack.pop().data)
        self.reset()
        return totalSum

    def printProduct(self):
        total = self.mathStack.peek().data
        self.saveStack.push(self.mathStack.pop().data)
        while self.mathStack.isEmpty() == False:
            total = total * self.mathStack.peek().data
            self.saveStack.push(self.mathStack.pop().data)
        self.reset()
        print("Product = " + str(total))

    def printMean(self):
        if self.totalCount() == 0:
            print("No items in list")
            return
        print("Mean = " + str(self.sum()/self.totalCount()))

    def printMin(self):
        if self.totalCount() == 0:
            print("No items in list")
            return
        smolBoi = self.mathStack.peek().data
        while self.mathStack.isEmpty() == False:
            if self.mathStack.peek().data < smolBoi:
                smolBoi = self.mathStack.peek().data
                self.saveStack.push(self.mathStack.pop().data)
            else:
                self.saveStack.push(self.mathStack.pop().data)
        self.reset()
        print("Min = " + str(smolBoi))

    def printMax(self):
        if self.totalCount() == 0:
            print("No items in list")
            return
        bigBoi = self.mathStack.peek().data
        while self.mathStack.isEmpty() == False:
            if self.mathStack.peek().data > bigBoi:
                bigBoi = self.mathStack.peek().data
                self.saveStack.push(self.mathStack.pop().data)
            else:
                self.saveStack.push(self.mathStack.pop().data)
        self.reset()
        print("Max = " + str(bigBoi))

    def reset(self):
        while self.saveStack.isEmpty() == False:
            self.mathStack.push(self.saveStack.pop().data)
