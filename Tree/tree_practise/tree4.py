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

if __name__=="__main__":
   node=Node(12)
   l=[22,18,15,20,24,6,4,1,5,10]
   for i in l:
       node.insert(i)
   print("The post order traversal of the tree is:")
   node.postorder()

              