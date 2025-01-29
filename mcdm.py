# C:\Users\USUARIO\Documentos\U\Math>

allFactors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
myFactors = [ ]
#  this is new changes from a new branch
# now its true

def end(x,y):
    print(f"yeahhhhhh:{x} {y}")


def gcd(x,y):
    if x and y == 1:
             print(myFactors)
             return end(x,y)
    else:
        for factor in allFactors:
         reminderX = x % factor
         reminderY = y % factor
         
         if reminderX  == 0:
            x = int(x / factor)
         if reminderY == 0:
            y = int(y / factor)
        
         if reminderX or reminderY == 0:
            myFactors.append(factor)
            return gcd(x, y)

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
myNumber = gcd(21,14)


