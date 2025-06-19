# Functions a named codeblock that performs a sequence of  actions when called

def hello(name):
    print(f"Hello {name} I'm learning about functions")


hello("Kimani")

def greeting(first_name, age):
    print(f"Hello {first_name} your age is {age}")
greeting(age=19,first_name="Vincent")

# def sum_all(args):
#     print(sum(args))

# sum_all(1,2,3,4,5)

colors=['red', 'blue', 'green', 'yellow']

for i in range(len(colors)):
    print(colors[i])