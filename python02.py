num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

def add(num1,num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def modulus(num1,num2):
    return num1%num2

def comparison(num1,num2):
    if num1 > num2:
        print (num1,">",num2)
    elif num2 >num1:
        print (num2,">",num1)
    else:
        print (num1,"=",num2)

print ("sum of numbers is",add(num1,num2))
print ("Difference of numbers is",substract(num1,num2))
print ("Product of numbers is",multiply(num1,num2))
print ("Dividing the numbers gives",divide(num1,num2))
print ("Modulus of numbers is",modulus(num1,num2))
comparison(num1,num2)