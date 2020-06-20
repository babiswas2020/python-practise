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

   def find_leaf(self):
       def is_leaf(node):
          if not node:
             return False
          else:
             if node.left==None and node.right==None:
                return True
             return False
       stack=[]
       stack.append(self)
       temp=None
       while stack:
           temp=stack.pop()
           while temp and (not is_leaf(temp)):
                if temp.left:
                   stack.append(temp.left)
                if temp.right:
                   stack.append(temp.right)
                temp=stack.pop()
           if temp:
              if is_leaf(temp):
                 print(temp.value)

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
   l=[22,18,15,20,24,6,10,4,1,5]
   for i in l:
      node.insert(i)
   print("Print the inorder traversal of the tree")
   node.inorder()
   print("Print the leaf nodes of the tree")
   node.find_leaf()
