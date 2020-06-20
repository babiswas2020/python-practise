class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def inorder(self):
      root=self
      while root:
          if root.left==None:
            print(root.value)
            root=root.right
          else:
            curr=root.left
            while curr.right!=root and curr.right:
                 curr=curr.right
            if curr.right==root:
               curr.right=None
               print(root.value)
               root=root.right
            elif curr.right!=root:
                 curr.right=root
                 root=root.left

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
   l=[12,22,18,24,15,20,6,4,10,1,5]
   node=Node(12)
   for i in l:
      node.insert(i)
   node.inorder()


            