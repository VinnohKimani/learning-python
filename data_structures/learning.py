class MyArray:
    def __init__(self):
        self.dictionary ={}
        self.length = 0

    def push(self, *values):
     for value in values:
        self.dictionary[self.length] = value
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        self.length -= 1
        return self.dictionary.pop(self.length)
    
    def __repr__(self):
        return f"MyArray(dictionary={self.dictionary}, length={self.length})" + "\n" 


arr = MyArray()
arr.push(1)
arr.push(2)
arr.push(4, 5, 6, 7, 8, 9, 20, 50)
# removing and printing 2
# print(arr.pop())
print(arr.dictionary)
print(arr.length)
    