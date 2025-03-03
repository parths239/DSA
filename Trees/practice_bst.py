# intial tree node setup
class TreeNode:
  
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None
 
# intial BST setup   
class BinarySearchTree:
  
  def __init__(self):
    self.root = None

#add function    
  def add(self,value):
    
    if self.root is None:
      self.root = TreeNode(value)
    else:
      self.root = self.add_recursively(self.root,value)
    
  def add_recursively(self,node,value):
    
    if node is None:
       return TreeNode(value)
       
    elif value < node.data:
      node.left = self.add_recursively(node.left,value)
        
    elif value > node.data :
      node.right = self.add_recursively(node.right,value)
      
    return node

# search function
  def search(self, value):
    
      return self.search_recursive(self.root, value)
  
  def search_recursive(self, node, value):
    
    if node is None:
      return False
    elif node.data == value:
      return True
    elif node.data < value:
      return self.search_recursive(node.right,value)
    else:
      return self.search_recursive(node.left,value)

# In order traversal      
  def in_order_traversal(self):
    elements = []
    
    self.in_order_recursive(elements, self.root)

    return elements
  
  def in_order_recursive(self, array, node):
   
      if node:
        self.in_order_recursive(array, node.left)
        array.append(node.data)
        self.in_order_recursive(array, node.right)

#preorder traversal

  def pre_order_traversal(self):
    
    elements = []
    self.pre_oreder_recursive(self.root, elements)
    return elements
  
  def pre_oreder_recursive(self, node, elements):
    
    if node:
      elements.append(node.data)
      self.pre_oreder_recursive(node.left, elements)
      self.pre_oreder_recursive(node.right, elements)

#postOrder traversal

  def post_order_traversal(self):
    
    elements = []
    self.post_order_recursive(self.root, elements)
    return elements
  
  def post_order_recursive(self, node, elements):
    
    if node:
      self.post_order_recursive(node.left, elements)
      self.post_order_recursive(node.right, elements)
      elements.append(node.data)
  
# delete function
  def delete(self, value):
    self.root = self.delete_recursive(self.root,value)
  
  def delete_recursive(self, node, value):
    
    if node is None:
      return None
    
    elif value < node.data:
      node.left = self.delete_recursive(node.left, value)
    
    elif value > node.data:
      node.right = self.delete_recursive(node.right, value)
    
    else:
      # we found the node and now we look at different cases
      # case 1: the node doesn't have any child
      if node.left is None and node.right is None:
        return None
      # case 2: only one child
      elif node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      # case 3: has both children
        #option 1: return smallest element in right subtree and delete it
      min_value = self.find_min(node.right) 
      node.data = min_value
      node.right = self.delete_recursive(node.right,min_value)
        #option 2: return largest element in left subtree and delete it
      # max_value = self.find_max(node.left)
      # node.data = max_value
      # self.delete_recursive(node.left,max_value)   
    
    # this finally returns updated self.root to the OG self.root
    return node  

# find min
  def find_min(self, node):
    while node.left:
      node = node.left
    return node.data

#find max
  def find_max(self, node):
    while node.right:
      node = node.right
    return node.data

# main function     
if __name__ == "__main__":
  
  valueArray = [13,5,11,6,17,9,10,21,20,19]
  # valueArray = [1,2,3,4,5,6,7]
  
  GajabTree = BinarySearchTree()
  
  for element in valueArray:
    GajabTree.add(element)
    
  print(GajabTree.in_order_traversal())
  # print(GajabTree.pre_order_traversal())
  # print(GajabTree.post_order_traversal())
  print(GajabTree.search(13))
  print(GajabTree.search(15))
  print(GajabTree.search(11))
  
  GajabTree.delete(9)
  GajabTree.delete(11)
  print(GajabTree.in_order_traversal())
  