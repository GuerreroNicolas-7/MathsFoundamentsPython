# C:\Users\USUARIO\Documentos\U\Math>

allFactors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
# allFactors = [2,3,4]
myFactors = [ ]
myCommonFactors = []
#  this is new changes from a new branch
# now its true

def end():
     unique_numbers_lcm = list(set(myFactors))
     print (unique_numbers_lcm)
     unique_numbers_gcd = list(set(myCommonFactors))
     print (unique_numbers_gcd)
     result = 1
     r = 1
     for factor in unique_numbers_lcm:
          result *= factor
     print(f"The LCM of 21 and 14 is: {result}")
     
     for f in unique_numbers_gcd:
        r *= f
     print(f"The GCD of 21 and 14 is: {r}")  
          

def gcd(x,y):
    print(x,y)
    if x == 1 and y == 1:
            
             return end()
    else:
        for factor in allFactors:
             xRemainder =   int(x % factor)
             yRemainder = int(y % factor)
             if xRemainder == 0 and yRemainder == 0: 
                  myCommonFactors.append(factor)
             if xRemainder == 0 or yRemainder == 0:
                  myFactors.append(factor)
                  if xRemainder == 0:
                       xDiv = int(x / factor)
                       return gcd(xDiv,y)
                  else: 
                        yDiv = int(y / factor)
                        return gcd(x,yDiv)
                    
             
# def firstDivition(x):
#     for factor in allFactors:
#         reminder = x % factor
#         if reminder == 0:
#             div = int(x / factor)
#             myFactors.append(factor)
#             if div == 1:
#                 return end(div)
#             else:
#                  print("oh not")
myNumber = gcd(10,20)


