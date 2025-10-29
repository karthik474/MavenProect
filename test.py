# import sys

# def add(num1, num2):
#     add = num1 + num2
#     return add

# def sub(num1, num2):
#     sub = num1 - num2
#     return sub

# def mul(num1, num2):
#     mul = num1 * num2
#     return mul

# num1 = float(sys.argv[1])
# operation = sys.argv[2]
# num2 = float(sys.argv[3])

# if operation == "sub":
#     output = sub(num1, num2)
#     print(output)


# ================

# import sys

# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[5])  
# operations = sys.argv[2:-1]

# for op in operations:
#     if op == "add":
#         result = add(num1, num2)
#     elif op == "sub":
#         result = sub(num1, num2)
#     elif op == "mul":
#         result = mul(num1, num2)
#     else:
#         print(f"Unknown operation: {op}")
#         continue

#     print(f"{op}: {result}")
