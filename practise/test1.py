class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def leaf_node(self):
       stack=[]
       temp=self
       stack.append(self)
       def is_leaf(node):
           if not node:
             return False
           else:
              if node.left==None and node.right==None:
                 return True
              else:
                 return False
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
   node.insert(21)
   node.insert(18)
   node.insert(24)
   node.insert(15)
   node.insert(20)
   node.insert(6)
   node.insert(10)
   node.insert(4)
   node.insert(2)
   node.insert(5)
   print("Print the leaf nodes:")
   node.leaf_node()
  

