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
# print(list[2:3])

# list = ["kar", "mar", "jar", "par"]
# list.append("sir")
# print(len(list))
# print(list)
#================

# list = [10, 3, 5]
# list.sort()
# print(list)
#=================
# x = 3

# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")
#=================================

# for i in range(10):
#     print(i)
# for _ in range(10):
#     print("mama")
#======================
# be = (man, cam, dan)
# for x in be:
#     print(x)
    
#=========
# import subprocess

# # Get all pod names in the current namespace
# result = subprocess.run(
#     ["kubectl", "get", "pods", "--no-headers", "-o", "custom-columns=:metadata.name"],
#     capture_output=True,
#     text=True
# )

# # Split output into a list of pod names
# pods = result.stdout.strip().split("\n")

# # Loop through each pod
# for pod in pods:
#     print(f"Processing pod: {pod}")
#     # Describe the pod (or any other kubectl command)
#     subprocess.run(["kubectl", "describe", "pod", pod])
#===============================

# numbers = [1, 2, 3, 4, 5, 6]

# for number in numbers:
#     if number == 1:
#         print("found 1")
#         break
# else:
#     print("not found 1")
#==================
# numbers = [1, 2, 3, 4, 5,]
# for num in numbers:
#     if num == 3:
#         print(num)
        # continue
    # print(num)
#==============================
  