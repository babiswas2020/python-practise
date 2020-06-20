class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

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
           root=stack.pop()
           print(root.value)
           if root.right:
              stack.append(root.right)
           if root.left:
              stack.append(root.left)

   def postorder(self):
       stack=[]
       root=self
       while True:
           if root:
              stack.append(root)
              root=root.left
           else:
              if not stack:
                 break
              if stack[-1].right==None:
                 root=stack.pop()
                 print(root.value)
                 while stack[-1].right==root:
                       root=stack.pop()
                       print(root.value)
                       if not stack:
                          break
              if stack:
                 root=stack[-1].right
              else:
                 break
             
       
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
          print("Duplication is not allowed")

if __name__=="__main__":
   node=Node(12)
   node.insert(22)
   node.insert(18)
   node.insert(24)
   node.insert(15)
   node.insert(20)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(1)
   node.insert(5)
   print("The inorder travaersal of the tree:")
   node.inorder()
   print("The postorder traversal of the tree:")
   node.postorder()
   print("The preorder traversal of the tree:")
   node.preorder()


   