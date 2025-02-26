class BinaryTreeNode:
  
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
  
  
  #inserts element into the tree
  def add_child(self, data):
        if self.data == data:
          return # do nothing
        
        if data > self.data:
          if self.right:
            self.right.add_child(data)
          else:
            self.right = BinaryTreeNode(data)
        
        else:
          if self.left:
            self.left.add_child(data)
          else:
            self.left = BinaryTreeNode(data)
    
  # does in order traversal
  def in_order_traversal(self):
    
    elements = []
    
    if self.left:
      elements = elements + self.left.in_order_traversal()
    
    elements.append(self.data)
    
    if self.right:
      elements = elements + self.right.in_order_traversal()
    
    return elements

  # returns true or false if the element is in the tree
  def search(self, value):
    if self.data == value:
      return True
    
    if value < self.data:
      if self.left:
        return self.left.search(value)
    
    else:
      if self.right:
        return self.right.search(value)
      
    return False
  
  # finds minimum element in entire binary tree
  def find_min(self): 
    if self.left:
      return self.left.find_min()
    else:
      return self.data
  
  # finds maximum element in entire binary tree
  def find_max(self): 
    if self.right:
      return self.right.find_max()
    else:
      return self.data
    
  # calculates sum of all the elements
  def calculate_sum(self):
    total = 0 
    elements = self.in_order_traversal()
    
    for i in elements:
      total = total + i
  
    return total
  
  # does pre order traversal  
  def pre_order_traversal(self):
    
    elements = []
    
    elements.append(self.data)
    
    if self.left:
      elements = elements + self.left.pre_order_traversal()
    
    if self.right:
      elements = elements + self.right.pre_order_traversal()
    
    return elements
  
  # does post order traversal
  def post_order_traversal(self):
    
    elements = []
    
    if self.left:
      elements = elements + self.left.post_order_traversal()
    
    if self.right:
      elements = elements + self.right.post_order_traversal()
    
    elements.append(self.data)
    
    return elements

  def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
     

if __name__ == "__main__":
  
  root = BinaryTreeNode(15)
  
  # root.add_child(2)
  # root.add_child(7)
  # root.add_child(3)
  # root.add_child(8)
  # root.add_child(10)
  # root.add_child(1)
  # root.add_child(9)
  
  root.add_child(12)
  root.add_child(27)
  root.add_child(7)
  root.add_child(14)
  root.add_child(20)
  root.add_child(88)
  root.add_child(23)
  
  
  
  
  print(root.in_order_traversal())
  print(root.search(2))
  print(root.find_min())
  print(root.find_max())
  print(root.calculate_sum())
  print(root.pre_order_traversal())
  print(root.post_order_traversal())
  
  # root.remove(23)
  # print(root.in_order_traversal())
  