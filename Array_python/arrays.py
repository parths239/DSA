# class Array:
#    def __init__(self, capacity):
#        self.capacity = capacity
#        self.arr = [0] * capacity
#        self.length = 0


#    def insert_end(self, n):
#        if self.length < self.capacity:
#            self.arr[self.length] = n
#            self.length += 1
#        else:
#            print("Array is already full")


#    def remove_end(self):
#        if self.length > 0:
#            self.arr[self.length - 1] = 0
#            self.length -= 1
#        else:
#            print("Array is empty")


#    def insert_at_index(self, index, val):
#        if self.length < self.capacity and 0 <= index <= self.length:
#            for x in range(self.length - 1, index - 1, -1):
#                self.arr[x + 1] = self.arr[x]
#            self.arr[index] = val
#            self.length += 1
#        else:
#            print("Array is full or index out of bounds")


#    def remove_at_index(self, index):
#        if 0 <= index < self.length:
#            for x in range(index, self.length - 1):
#                self.arr[x] = self.arr[x + 1]
#            self.arr[self.length - 1] = 0  # Clear the last element
#            self.length -= 1
#        else:
#            print("Index is out of bounds")


#    def print_array(self):
#        for i in range(self.length):
#            print(self.arr[i], end=", " if i < self.length - 1 else "")
#        print()




# # Testing the Array class
# trial_array = Array(5)


# trial_array.insert_end(10)
# trial_array.insert_end(15)
# trial_array.insert_end(22)
# trial_array.print_array()  # Output: 10, 15, 22


# trial_array.remove_end()
# trial_array.print_array()  # Output: 10, 15


# trial_array.insert_at_index(2, 40)
# trial_array.insert_at_index(0, 30)
# trial_array.print_array()  # Output: 30, 10, 40, 15


# trial_array.remove_at_index(2)
# trial_array.print_array()  # Output: 30, 10, 15
































# Dynamic Array:

# # Python arrays are dynamic by default, but this is an example of resizing.
# class Array:
#    def __init__(self):
#        self.capacity = 2
#        self.length = 0
#        self.arr = [0] * 2 # Array of capacity = 2


#    # Insert n in the last position of the array
#    def pushback(self, n):
#        if self.length == self.capacity:
#            self.resize()
          
#        # insert at next empty position
#        self.arr[self.length] = n
#        self.length += 1


#    def resize(self):
#        # Create new array of double capacity
#        self.capacity = 2 * self.capacity
#        newArr = [0] * self.capacity
      
#        # Copy elements to newArr
#        for i in range(self.length):
#            newArr[i] = self.arr[i]
#        self.arr = newArr
      
#    # Remove the last element in the array
#    def popback(self):
#        if self.length > 0:
#            self.length -= 1
  
#    # Get value at i-th index
#    def get(self, i):
#        if i < self.length:
#            return self.arr[i]
#        # Here we would throw an out of bounds exception


#    # Insert n at i-th index
#    def insert(self, i, n):
#        if i < self.length:
#            self.arr[i] = n
#            return
#        # Here we would throw an out of bounds exception      


#    def print(self):
#        for i in range(self.length):
#            print(self.arr[i])
#        print()





# Stack:
# # Implementing a stack is trivial using a dynamic array
# # (which we implemented earlier).
# class Stack:
#    def __init__(self):
#        self.stack = []


#    def push(self, n):
#        self.stack.append(n)


#    def pop(self):
#        return self.stack.pop()