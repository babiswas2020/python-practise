class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def postorder(self):
       if self:
          if self.left:
             self.left.postorder()
          if self.right:
             self.right.postorder()
          print(self.value)

   def preorder(self):
       if self:
         print(self.value)
         if self.left:
            self.left.preorder()
         if self.right:
            self.right.preorder()

   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

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
   node.insert(24)
   node.insert(15)
   node.insert(20)
   node.insert(6)
   node.insert(10)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   print("The inorder traversal of the node is:")
   node.inorder()
   print("The preorder traversal of the tree is:")
   node.preorder()
   print("The postorder traversal of the tree is:")
   node.postorder()


