
Coeficients = []
listTermSum  = []

elements = [ ]

# Get Coeficients according to the exponent 


def coefPerlvl(exp):
    for i in range(exp - 1):
        elements.append(Coeficients[i] + Coeficients[i + 1])
    return newColist(exp)


def newColist(exp):
    global Coeficients
    global elements
    NewColist= [1]

    for e in elements:
        NewColist.append(e)
    
    if exp > 0:
        NewColist.append(1)
    Coeficients = NewColist.copy()
    elements = []
    
    

def binominal(a,b,type,exp):
    for i in range(exp + 1):
        coefPerlvl(i)
    return sumCoAB(a,b,type,exp)
        

# Calculation Final result
def sumCoAB(a,b, type , exp):
    expA = exp
    expB = 0 
    for co in Coeficients:
         listTermSum.append(co * ((a**expA) * (b**expB)))
         print(listTermSum)
         expA -= 1
         expB += 1
    print(listTermSum)
    return finalTermRest(a,b,type)

def finalTermSum():
    result = 0
    for s in listTermSum:
        result += s
    print(result)



def finalTermRest(a,b , type):
    if type == "+":
       return finalTermSum()

    elif type == "-":
        result = 0
        sign = 0
        
        for s in listTermSum:
            
            if sign % 2 == 0:
                result += s
            else:
                result -= s
            sign +=1

        print(result)
    else: 
        print("Error")     
   






binominal(1,3,"-", 1)













