class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

   def lca(self,val1,val2):
          if val1>self.value and val2>self.value:
              if self.right:
                 return self.right.lca(val1,val2)
          elif val1<self.value and val2<self.value:
              if self.left:
                 return self.left.lca(val1,val2)
          elif val1>self.value and val2<self.value:
                 return self
          elif val1<=self.value and val2>=self.value:
                 return self
              
          
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
   node.insert(10)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   print("The inorder traversal of the node is:")
   node.inorder()
   print("Find the lca for the nodes 20 and 24")
   print(node.lca(20,24).value)


