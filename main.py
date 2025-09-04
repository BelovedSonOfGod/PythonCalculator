'''

Shunting-yard of Dijkstra algorithm

For the future in case I want to add parenthesis
'''
class Node:
    def __init__(self,val,next):
        self.value=val
        self.next=next



class Stack:
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
        self.stackOfAdditionSubstraction=Stack()

    def checkNextSignForDelayedOperation(self,i:int)->bool:
        '''
        For delaying pushing to stack in case is multiplication or division for example
        '''
        if self.operationString[i]=="*" or self.operationString[i]=="/":
            return True
        else:
            return False


    def tokenize(self):
        tokens = []
        i = 0
        sign=1
        while i < len(self.operationString):
            ch = self.operationString[i]
            
            # Ignore spaces
            if ch == " ":
                i += 1
                continue
            
            # Negative or decimal number
            if ch.isdigit() or ch == "-" or (ch in "+-" and (i == 0 or self.operationString[i-1] in "*/+-")):
                num = ch
                i += 1
                has_decimal = (ch == ".")
                while i < len(self.operationString) and (self.operationString[i].isdigit() or self.operationString[i] == "."):
                    if self.operationString[i] == ".":
                        if has_decimal:
                            raise ValueError("Invalid number with two decimals")
                        has_decimal = True
                    num += self.operationString[i]
                    i += 1
                tokens.append(num)
                continue
            
            # Operators
            if ch in "+-*/()":
                tokens.append(ch)
                i += 1
                continue
            
            raise ValueError(f"Unexpected character: {ch}")
        
        return tokens
    

    

    def processMulDiv(self):
        '''
        Save in a stack the order of operations for additions and substractions but for multiplications and divisions
        Resolve it inmediatly, and then save it on the stack
        '''
        tokens=self.tokenize()
        i=0
        while i < len(tokens):
            if tokens[i]=="-":
                self.stackOfAdditionSubstraction.push(float(tokens[i+1]))
            elif tokens[i]=="+":
                self.stackOfAdditionSubstraction.push(float(tokens[i-1]))
            elif tokens[i]=="*":
                self.stackOfAdditionSubstraction.push(float(tokens[i-1])*float(tokens[i+1])) ##Assign the final amoount between the 2 parts
            elif tokens[i]=="/":
                self.stackOfAdditionSubstraction.push(float(tokens[i-1])/float(tokens[i+1])) ##Assign the final amoount between the 2 parts
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
        self.processMulDiv()
        return self.AddSubstractQueue()



if __name__ == "__main__":
    stringWithOperation="-3.5 + 4 * -2"
    result=Calculator(stringWithOperation)
    print(result.Resolve())

    