## 1. Key Differences Between List and Dictionary

| Feature      | List                              | Dictionary                          |
|--------------|----------------------------------|-------------------------------------|
| **Structure** | Ordered collection of items      | Key-value pairs                     |
| **Access**    | By index (`0, 1, 2…`)           | By key                              |
| **Syntax**    | `[item1, item2, ...]`           | `{key1: value1, key2: value2}`     |
| **Duplicate** | Allowed                          | Keys must be unique                 |
| **Use case**  | Sequence of items                | Mapping of keys to values           |

---

## 2. Real-world Python for DevOps Examples

- **GitHub Webhooks** – Automate CI/CD pipelines.
- **JIRA Integration** – Automate ticket creation and updates.
- **File Operations** – Automate configuration or log file management.

**Challenges & Solutions:**
- Challenge: Managing API authentication securely.  
  Solution: Use environment variables, input variables, or command-line arguments instead of hardcoding credentials.

---

## 3. Securing Python Code

- Avoid storing sensitive data in plain text.
- Use **environment variables**, **input arguments**, or **command-line parameters**.
- Limit access to configuration files.

---

## 4. Mutable vs Immutable Objects

- **Mutable:** Can be modified after creation (e.g., lists).  
- **Immutable:** Cannot be modified after creation (e.g., tuples).

```python
# Mutable
my_list = [1, 2, 3]
my_list[0] = 0
print(my_list)  # Output: [0, 2, 3]

# Immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 0  # Error
5. List vs Tuple
List: Mutable, dynamic.

Tuple: Immutable, fixed.

python
Copy code
# List
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# Tuple
my_tuple = (1, 2, 3)
# my_tuple.append(4)  # Error
6. Virtualenv
Creates isolated Python environments for different projects.

bash
Copy code
# Create virtual environment
virtualenv myenv

# Activate
# Windows
myenv\Scripts\activate
# Unix/MacOS
source myenv/bin/activate
7. Decorators
Decorators modify or extend the behavior of functions.

python
Copy code
def my_decorator(func):
    def wrapper():
        print("Before the function.")
        func()
        print("After the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
8. Exception Handling
python
Copy code
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
9. append() vs extend()
python
Copy code
# append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# extend()
my_list.extend([5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
10. Lambda Functions
Anonymous functions for short tasks.

python
Copy code
square = lambda x: x ** 2
print(square(5))  # Output: 25
11. Loops
python
Copy code
# For loop
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1
12. == vs is
== compares values.

is checks object identity.

python
Copy code
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

c = a
print(a is c)  # True
13. pass Keyword
Placeholder when no action is needed.

python
Copy code
def placeholder_function():
    pass  # To be implemented later
14. Global vs Local Variables
python
Copy code
# Global
global_var = 10
def my_function():
    print(global_var)
my_function()  # 10

# Local
def another_function():
    local_var = 5
    print(local_var)
another_function()  # 5
# print(local_var)  # Error
15. open() vs with open()
open() → Must manually close.

with open() → Automatically closes file.

python
Copy code
# Using open()
file = open('example.txt', 'r')
content = file.read()
file.close()

# Using with open()
with open('example.txt', 'r') as file:
    content = file.read()
# File is auto-closed
