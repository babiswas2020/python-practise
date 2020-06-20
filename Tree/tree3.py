class Node:
  def __init__(self,value):
      self.value=value
      self.left=None
      self.right=None

  def postorder(self):
      stack1=[]
      stack2=[]
      root=self
      stack1.append(root)
      while stack1:
          m=stack1.pop()
          stack2.append(m)
          if m.left:
             stack1.append(m.left)
          if m.right:
             stack1.append(m.right)
      while stack2:
         print(stack2.pop().value)

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
   node.insert(20)
   node.insert(15)
   node.insert(24)
   node.insert(6)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   node.insert(10)
   print("The postorder traversal of the node is:")
   node.postorder()

