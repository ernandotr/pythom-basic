# Functions

# Simple
def greeting():
    print("Hello, welcome to python.")

greeting()

# Function with parameters
def greeting(name):
    print(f"Helli, {name}")

greeting("Ernando")

# Function returnig value
def msum(a, b):
    return a + b;

result = msum(5, 3)
print(f"Result: {result}")

# Function with default parameter
def greeting(name="Visitor"):
    print(f"Hello, {name}")
greeting()

# Converting

x = "10"
y = 5
# print(x + y) It doesn't work
print(int(x) + y) # It works


def my_sum(*numbers):
    return sum(numbers)
result = my_sum(1, 2, 3, 4)
print(f"Result: {result}")

def show_info(**info):
    print(info)
    for key, value in info.items():
        print(f"{key}: {value}")
show_info(name = "Ernando", age="29")

# Lambda functions
# Simple 
def interest(x):
    return x * 1.03
print(interest(100))

#Lambda
interest2 = lambda x: x * 1.03
print(interest2(1000))

