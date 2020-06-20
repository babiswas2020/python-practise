class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def find_path(self,stack):
      def display(stack):
         if stack:
            print([i.value for i in stack])
         return

      if not self:
         return
      stack.append(self)
      if self.left:
         self.left.find_path(stack)
      display(stack)
      if self.right:
         self.right.find_path(stack)
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
   node=Node(12)
   node.insert(22)
   node.insert(18)
   node.insert(15)
   node.insert(20)
   node.insert(24)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(1)
   node.insert(5)
   print("The path from root to all nodes")
   stack=[]
   node.find_path(stack)
   
   
