
class Node:
    def __init__(self,val,next):
        self.value=val
        self.next=next



class MinimumStack:
    def __init__(self):
        self.head=None
    def push(self,val:float):
        if self.head==None:
            self.head=Node(val,None)
        else:
            newNode=Node(val,None)
            newNode.next=self.head
            self.head=newNode
    def pop(self):
        if self.head==None:
            return None
        valueToReturn=self.head.value
        self.head=self.head.next
        return valueToReturn
    


class Calculator:
    def __init__(self,operation:str):
        self.result=0.0
        self.operationString=operation
        self.stackOfAdditionSubstraction=MinimumStack()
    
    def getNumbersInQueueAndResolveMultiplyDivide(self):
        IsNegative=False
        NumberFound=""
        for i in range(len(self.operationString)):
            if self.operationString[i].isdigit():
                NumberFound+=self.operationString[i]
            elif self.operationString[i]=="-":
                IsNegative=True
                NumberFound=""
                try:
                    if IsNegative:
                        self.stackOfAdditionSubstraction.push(-float(NumberFound))
                    else:
                        self.stackOfAdditionSubstraction.push(float(NumberFound))
                except ValueError:
                    self.stackOfAdditionSubstraction.push(0)
            elif self.operationString[i]=="+":
                try:
                    if IsNegative:
                        self.stackOfAdditionSubstraction.push(-float(NumberFound))
                    else:
                        self.stackOfAdditionSubstraction.push(float(NumberFound))
                except ValueError:
                    self.stackOfAdditionSubstraction.push(0)
                IsNegative=False
                NumberFound=""
            elif self.operationString[i]=="*":
                Number2=""
                for j in range(i+1,len(self.operationString)):
                    if self.operationString[j].isdigit():
                        Number2+=self.operationString[j]
                    else:
                        break
                    try:
                        if IsNegative:
                            self.stackOfAdditionSubstraction.push(-float(NumberFound)*float(Number2))
                        else:
                            self.stackOfAdditionSubstraction.push(float(NumberFound)*float(Number2))
                    except ValueError:
                        self.stackOfAdditionSubstraction.push(0)
                    i=j

                IsNegative=False
                NumberFound=""
                Number2=""
            elif self.operationString[i]=="/":
                Number2=""
                for j in range(i+1,len(self.operationString)-i):
                    if self.operationString[j].isdigit():
                        Number2+=self.operationString[j]
                    else:
                        break
                try:
                    if IsNegative:
                        self.stackOfAdditionSubstraction.push(-float(NumberFound)/float(Number2))
                    else:
                        self.stackOfAdditionSubstraction.push(float(NumberFound)/float(Number2))
                except ValueError:
                    self.stackOfAdditionSubstraction.push(0)
                i=j

                IsNegative=False
                NumberFound=""
    def AddSubstractQueue(self):
        finalResult=0.0
        while True:
            amountOfStack=self.stackOfAdditionSubstraction.pop()
            if amountOfStack==None:
                break
            finalResult+=amountOfStack
        return finalResult

    def Resolve(self):
        self.getNumbersInQueueAndResolveMultiplyDivide()
        return self.AddSubstractQueue()



if __name__ == "__main__":
    stringWithOperation="-23+3*3"
    result=Calculator(stringWithOperation)
    print(result.Resolve())

    