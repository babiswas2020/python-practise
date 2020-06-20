class Node:
     def __init__(self,value):
         self.value=value
         self.left=None
         self.right=None
     def search(self,value):
         temp=temp1=None
         if not self:
            return None
         else:
            if self.value==value:
               return self
            else:
               if self.left:
                  temp=self.left.search(value)
               if self.right:
                  temp1=self.right.search(value)
               if temp:
                  return temp
               elif temp1:
                  return temp1
                  
     def min(self,node):
         root=node
         if not root:
            return None
         while root.left!=None:
             root=root.left
         return root

     def inorder_sucessor(self,node):
         if node.right:
            return self.min(node.right)
         else:
            root=self
            temp=None
            while root:
               if root.value>node.value:
                  temp=root
                  root=root.left
               elif root.value<node.value:
                  root=root.right
               else:
                  return temp
                
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
   node.insert(24)
   node.insert(18)
   node.insert(20)
   node.insert(15)
   node.insert(6)
   node.insert(10)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   print("The sucessor of the value 15 is:")
   node1=node.search(15)
   print(node1.value)
   print(node.inorder_sucessor(node1).value)

