def bagi(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: Tried to divide by zero"

print(bagi(4,2)) # output: 2
print(bagi(10,0)) # output: "Error: Tried to divide by zero"