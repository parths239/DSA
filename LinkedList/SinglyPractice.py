class Node:
  def __init__(self,value, next = None):
    self.value = value
    self.next = next
    

class LinkedList:
  
  def __init__(self):
    self.head = Node(-1)
    self.tail = self.head
    
  def get(self, index: int) -> int:
    curr = self.head.next
    i = 0
    
    while curr:
      if i == index:
        return curr.value

      curr = curr.next
      i+=1
    
    return -1
  
  def insert_head(self, value: int) -> None:
    
    newNode = Node(value)
    
    newNode.next = self.head.next
    self.head.next = newNode
    
    if self.tail == self.head:
      self.tail = newNode
      
  def insert_tail(self, value: int) -> None:
    newNode = Node(value)
    self.tail.next = newNode
    self.tail = newNode
    
  def remove(self, index: int) -> bool:
    i = 0
    curr = self.head
    
    while curr and i < index:
      curr = curr.next
      i+=1
    
    if curr and curr.next:
      curr.next = curr.next.next
      return True
    
    return False
  
  def get_values(self) -> list[int]:
    
    curr = self.head.next
    i = 0
    
    array = []
    
    while curr:
      array.append(curr.value)
      curr = curr.next
      
    return array
    
    
    