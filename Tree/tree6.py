class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

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

   def height(self):
       count=0
       queue=[]
       queue.append(self)
       while queue:
           q_len=len(queue)
           if q_len:
              count=count+1
           else:
              break
           while q_len:
              m=queue.pop(0)
              if m.left:
                queue.append(m.left)
              if m.right:
                queue.append(m.right)
              q_len=q_len-1
       return count
   
           
   def inorder(self):
      if self:
         if self.left:
            self.left.inorder()
         print(self.value)
         if self.right:
            self.right.inorder()

if __name__=="__main__":
   node=Node(12)
   node.insert(22)
   node.insert(18)
   node.insert(20)
   node.insert(15)
   node.insert(24)
   node.insert(6)
   node.insert(4)
   node.insert(10)
   node.insert(1)
   node.insert(5)
   print("The height of the tree is")
   print(node.height())

   
