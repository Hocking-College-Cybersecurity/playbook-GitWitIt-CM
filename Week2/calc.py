print("My Python Calculator")

num1 = float(input("Enter first number"))

while(True):
    try:
        num2 = float(input("Enter second number"))
        
        if num2 == 0:
            print("INvalid input: CAnnot divide by 0")
            continue
        else:
            break
    
    except ValueError:
        print("INvalid input: enter another number")

add_result = num1 + num2
subtract_result = num1 - num2
multiply_result = num1 * num2
divide_result = num1 / num2

print(f"{num1}+{num2}={add_result}")
print(f"{num1}-{num2}={subtract_result}")
print(f"{num1}*{num2}={multiply_result}")
print(f"{num1}/{num2}={divide_result}")



