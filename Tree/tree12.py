class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def level_trav(self):
      queue=[]
      queue.append(self)
      while queue:
         m=queue.pop(0)
         print(m.value)
         if m.left:
            queue.append(m.left)
         if m.right:
            queue.append(m.right)

   def mirror(self):
       temp1=temp2=None
       if not self:
          return self
       else:
           root=self
           if root.left:
              temp1=root.left
           if root.right:
              temp2=root.right
           if root.left:
              root.left=temp2
           if root.right:
              root.right=temp1
           if root.left:
              root.left.mirror()
           if root.right:
              root.right.mirror()
           
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
   node.insert(6)
   node.insert(18)
   node.insert(15)
   node.insert(20)
   node.insert(24)
   node.insert(10)
   node.insert(4)
   node.insert(1)
   node.insert(5)
   print("The level order traversal of the tree :")
   node.level_trav()
   print("The mirror of the given tree is:")
   node.mirror()
   print("the level order traversal of the modified tree is:")
   node.level_trav()

   
