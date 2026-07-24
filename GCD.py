numberL = int(input("Enter the first number: "))
numberS = int(input("Enter the second number: "))

while (numberS):
    numberST = numberS
    numberS = numberL % numberS
    numberL = numberST

print("HCF is :", numberL)