num1 = input("number1: ")
num1 = int(num1)
num2 = input("number2: ")
num2 = int(num2)

def evclid(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

num = evclid(num1,num2)
print(num)