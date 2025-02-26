class TreeNode:
  
  def __init__(self,data):
    self.data = data
    self.right = None
    self.left = None
    
class BinarySearchTree:
  
  def __init__(self):
    self.root = None
    
  def add(self,value):
    
    if self.root is None:
      self.root = TreeNode(value)
    else:
      self.add_recursively(self.root,value)
    
  def add_recursively(self,node,value):
    
    if node is None:
       node = TreeNode(value)
       
    elif node.data < value:
      self.add_recursively(node.right,value)
        
    elif node.data > value:
      self.add_recursively(node.left,value)
      