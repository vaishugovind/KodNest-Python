def mini_calculator(num1, num2, operation):
    if operation=="+":
        print(num1 + num2)
    elif operation=="-":
        print(num1 - num2)
    elif operation=="*":
        print(num1 * num2)
    elif operation=="/":
        print(num1 / num2)
    elif operation=="//":
        print(num1 // num2)
    elif operation=="%":
        print(num1 % num2)
    else:
        print("Invalid Operation")
mini_calculator(10, 20, "%" )