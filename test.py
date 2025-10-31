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
# ===========================

# import os 
# print(os.getenv("apitoken"))
# print(os.getcwd())
# os.listdir() 
# os.mkdir("test") 
#======================
# import sys
# type = sys.argv[1]

# if type == "m2.micro":
#     print("creating")
# else:
#     print("no create")
#===========
# a1 = "abv"
# b1 = "frfe"
# c1 = "frfe"
# list = [a1, b1, c1]
# print(list)
#=================

# a1 = "abv"
# b1 = "frfe"
# c1 = "frfe"
# list = [a1, b1, c1]
# for abc in list:
#     print(abc)
#===============
# list = ["kar", "mar", "jar", "par"]
# print(len(list))
#=======


# list = ["kar", "mar", "jar", "par"]
# del list[2:4]
# print(list)

# list = ["kar", "mar", "jar", "par"]
# list.remove("mar")
# print(len(list))

# list = ["kar", "mar", "jar", "par"]
# list.append("sir")
# print(len(list))
# print(list)
#================