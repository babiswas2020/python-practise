class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
       stack1=[]
       stack2=[]
       stack1.append(self)
       while stack1:
          m=stack1.pop()
          stack2.append(m)
          if m.left:
             stack1.append(m.left)
          if m.right:
             stack1.append(m.right)
       print([i.value for i in stack2])

   def inorder(self):
      stack=[]
      root=self
      while True:
         if root:
            stack.append(root)
            root=root.left
         elif stack:
            root=stack.pop()
            print(root.value)
            root=root.right
         else:
            break
         
   def preorder(self):
       stack=[]
       stack.append(self)
       while stack:
           m=stack.pop()
           print(m.value)
           if m.right:
              stack.append(m.right)
           if m.left:
              stack.append(m.left)

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
   node.insert(10)
   node.insert(4)
   node.insert(2)
   node.insert(5)
   print("Preorder traversal of the tree")
   node.preorder()
   print("Inorder traversal of the tree")
   node.inorder()
   print("Postorder traversal of the tree")
   node.postorder()

