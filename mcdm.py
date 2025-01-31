# cd  C:/Users/USUARIO/Documentos/U/Math
allFactors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
allMyFactors = [ ]
myCommonFactors = []



def getFactors(x,y):
    if x == 1 and y == 1:
             return
    else:
        for factor in allFactors:
            # Check if its factor for my numbers
             xRemainder =   int(x % factor)
             yRemainder = int(y % factor)
             # Get my common factors    
             if xRemainder == 0 and yRemainder == 0: 
                  myCommonFactors.append(factor)

              # Get all the factors  
             if xRemainder == 0 or yRemainder == 0:
                  allMyFactors.append(factor)
                  xDiv = x
                  yDiv = y
                  if xRemainder == 0:
                       xDiv = int(x / factor)
                       
                  if yRemainder == 0: 
                        yDiv = int(y / factor)
                  # return with at least a new value to break they down again 
                  return getFactors(xDiv,yDiv)


def mathMethods(methodtype):
     result = 1
     def inner_function():
          for factor in methodtype:
               nonlocal result
               result *= factor

          return result
     return inner_function


myNumbers = getFactors(10,5)
LCM = mathMethods(allMyFactors)
GCD = mathMethods(myCommonFactors)
print(GCD())
print(LCM())


# OWN HIGH PROCEDUAL CHALLENGING QUESTIONS
# what if I put for for a set empty?


