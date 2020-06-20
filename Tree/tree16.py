class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self,stack):
       if self:
          stack.append(self)
          if self.left:
             self.left.postorder(stack)
          if self.right:
             self.right.postorder(stack)
          print([i.value for i in stack])
          stack.pop()

   def insert(self,value):
      if self.value>value:
         if self.left:
            self.left.insert(value)
         else:
            self.left=Node(value)
      elif self.value<value:
         if self.right:
            self.right.insert(value)
         else:
            self.right=Node(value)
      else:
         print("Duplication not allowed")

if __name__=="__main__":
   stack=[]
   node=Node(12)
   node.insert(22)
   node.insert(24)
   node.insert(18)
   node.insert(20)
   node.insert(15)
   node.insert(6)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   node.insert(10)
   print("The path from root to node is:")
   node.postorder(stack)

