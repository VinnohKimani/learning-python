"""
---->A Stack is a linear data structure that allows you to store
  a list of data of some sort, and to add and remove values.
---->Values in the stack are processed in First In, Last Out (FILO) order

Stack Methods
The implementation of a Stack will vary depending on what's needed, but, at a minimum, generally includes the following methods:

-push: add an element to the top of the stack
-pop: remove the element at the top of the stack
-peek (or top): return the value of the element at the top of the stack without removing it

-empty/full: return true if the Stack is empty/full; false otherwise.
-search(target): return the distance between the top of the stack and the target element if it's present; -1 otherwise.
-size: return the number of elements contained in the Stack.
"""


def reverse_string(string):
    stack = []

    for char in string:
        stack.append(char)

    reversed = " "
    while stack:
        reversed += stack.pop()
    return reversed


print(reverse_string("Kimani"))

def evaluate_keystrokes(string):
    stack = []
    for char in string:
        # Every time we encounter the <, we "erase" the previous character but only if the stack 
        #  is not empty
        if char == "<":
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(char)

    result = ""
    while stack:
        result = stack.pop() + result

    return result
