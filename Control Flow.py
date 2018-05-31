
array=[]
file = input("Enter a file:  ") 
s = open(file, "r").read()

#Defining the stack for later use
class stack():
    def __init__(self): 
        self.l = []
        
    def length(self): 
        return len(self.l)
    
    def isEmpty(self):
        return len(self.l)==0

    def push(self,item): 
        self.l.append(item)
        
    def pop(self): 
        return self.l.pop()

    def peek(self): 
        return self.l[-1]


myStack = stack()
stackTrace = stack()
line_Number = 0

#Each branches are initially zero
class knot():
    def __init__(self):
        #initializing the string parser
        self.text = "" 
        self.level = 0
        self.parent = 0
        self.lineNum = 0
        self.id = 0
        self.start = 0

for i in range(len(s)):
    if s[i] == "\n":
        line_Number+=1
    elif s[i] == "{":
        myStack.push(i)
        stackTrace.push(line_Number)
    elif s[i] == "}":
        node = knot()
        node.level = myStack.length()
        node.start = mystack.peek()
        node.text = s[myStack.pop():i+1]
        if mystack.length()==0:
            node.parent = 0
        else:
            node.parent = mystack.peek()
        node.lineNum = stackTrace.pop()
        array.append(n)

def maxLimit(array):
    maximum = 0
    for i in array:
        if i.level > maximum:
            maximum = i.level
    return maximum
counter = 2
for j in range(1,maxLimit(array)+1):
    for i in array:
        if i.level == j:
            i.id = counter
            counter+=1
dictionary={}
for element in array:
    if element.parent not in dictionary:
        dictionary[element.parent] = [element.id]
    else:
        dictionary[element.parent].append(element.id)
    
#printdictionary

List = {} #placeholder for numbers

for keys in dictionary:
    if keys == 0:
        List[1] = dictionary[keys]
    for ele in array:
        if keys == ele.start:
           List[ele.id] = dictionary[keys]

#Here are number/list of the control flows

childNodes = []
childToParent = {}
for key in List:
    for i in List[key]:
        childToParent[e] = key
        if i not in List:
            childNodes.append(i)


for k in childNodes: 
    toprint = [k]
    current = k
    while(current in childToParent): #parsed using nodes
        current = childToParent[current]
        toprint.append(current)

    toprint.reverse()
    for knot in toprint:
        if knot == toprint[-1]:
            print(knot)
        else:
            print(knot, end = "....done!")

        















