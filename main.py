
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

    def getNextNumber(self, i):
        """
        Have a sign, check the sign and adjust it depending on it, then iterate and get all the numbers and return the sign multiplied by the number
        """
        IsDecimal=False
        sign = 1
        if i < len(self.operationString) and self.operationString[i] == "-":
            sign = -1
            i += 1
        elif i < len(self.operationString) and self.operationString[i] == "+":
            i += 1

        Number2 = ""
        while i < len(self.operationString) and (self.operationString[i].isdigit() or self.operationString[i] == "."):
            if self.operationString[i] == "." :
                if IsDecimal==True:
                    i += 1
                    continue
                else:
                    IsDecimal=True

            Number2+= self.operationString[i]
            i += 1

        return (sign * float(Number2), i)


    def getNumbersInQueueAndResolveMultiplyDivide(self):
        '''
        Save in a stack the order of operations for additions and substractions but for multiplications and divisions
        Resolve it inmediatly, and then save it on the stack
        '''
        NumberFound=""
        i=0
        while i < len(self.operationString):
            if self.operationString[i].isdigit():
                NumberFound+=self.operationString[i]
            elif self.operationString[i]=="-":
                Number2, i = self.getNextNumber(i)
                self.stackOfAdditionSubstraction.push(float(Number2))
                continue


            elif self.operationString[i]=="+":
                self.stackOfAdditionSubstraction.push(float(NumberFound))
                NumberFound=""
                continue
            elif self.operationString[i]=="*":
                Number2, i = self.getNextNumber(i+1)
                self.stackOfAdditionSubstraction.push(float(NumberFound)*float(Number2)) ##Assign the final amoount between the 2 parts
                NumberFound=""
                Number2=""
                continue
            elif self.operationString[i]=="/":
                Number2, i = self.getNextNumber(i+1)
                self.stackOfAdditionSubstraction.push(float(NumberFound)/float(Number2)) ##Assign the final amoount between the 2 parts
                NumberFound=""
                Number2=""
                continue
            i+=1
    def AddSubstractQueue(self):
        '''
        Loops the stack to sum everything there (the negative should already be saved as negative so that when added, it substracts automatically)
        '''
        finalResult=0.0
        while True:
            amountOfStack=self.stackOfAdditionSubstraction.pop()
            if amountOfStack==None:
                break
            finalResult+=amountOfStack
        return finalResult

    def Resolve(self):
        '''
        Call the function that saves the numbers in the stack and resolve the multiplciation-divisions
        and the function that sums-substracts everything on the stack
        '''
        self.getNumbersInQueueAndResolveMultiplyDivide()
        return self.AddSubstractQueue()



if __name__ == "__main__":
    stringWithOperation="-3.5*2"
    result=Calculator(stringWithOperation)
    print(result.Resolve())

    