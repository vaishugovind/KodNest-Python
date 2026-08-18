count = 10
def increase():
    global count
    count = 10
    count = count + 1
    return count
x = increase()
print(x)