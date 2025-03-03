
class Node:

   def __init__(self, value, next = None):
       self.value = value
       self.next = next


class LinkedList:
  
   def __init__(self):
       self.head = Node(-1)
       self.tail = self.head


  
   def get(self, index: int) -> int:
       i = 0
       curr = self.head.next


       while curr:
           if i == index:
               return curr.value
           i+=1
           curr = curr.next
       return -1
      


   def insertHead(self, value: int) -> None:
      
       newNode = Node(value)
       newNode.next = self.head.next
       self.head.next = newNode


       if self.tail == self.head:
           self.tail = newNode
      


   def insertTail(self, value: int) -> None:
       newNode = Node(value)
       self.tail.next = newNode
       self.tail = newNode
      


   def remove(self, index: int) -> bool:
       i = 0
       curr = self.head


       #so the trick is to start indexing a step before the "real"
       # indexing of linked list that way you stop when i = index which
       # would technically be right before the index


       while i < index and curr:
           i+=1
           curr = curr.next


       if curr and curr.next:
           #last element edge case
           if curr.next == self.tail:
               self.tail = curr
           curr.next = curr.next.next
           return True
       return False




   def getValues(self) -> list[int]:
       curr = self.head.next
       arr = []


       while curr:
           arr.append(curr.value)
           curr = curr.next
       return arr