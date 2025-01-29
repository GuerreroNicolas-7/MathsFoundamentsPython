# C:\Users\USUARIO\Documentos\U\Math>

allFactors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
myFactors = [ ]


def end(x):
    print(f"yeahhhhhh:{x}")
def gcd(x):
    for factor in allFactors:
        reminder = x % factor
        if reminder == 0:
            div = int(x / factor)
            myFactors.append(factor)
            if div == 1:
                print(myFactors)
                return end(div)
            else:
                return gcd(div)
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
myNumber = gcd(21)


