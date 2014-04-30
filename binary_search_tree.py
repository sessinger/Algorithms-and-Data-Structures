# Steve Essinger
# 3/5/14

'''
class Counter(object):
    def __init__(self,fun):
        self._fun = fun
        self.counter = 0
    def __call__(self,*args,**kwargs):
        self.counter +=1
        return self._fun(*args,**kwargs)
'''
class Node():
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self.size = 1
        
class BST():
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.height = 1
        else:
            self.insertNode(self.root,val)

    def insertNode(self,node,val,height=1):
        node.size += 1
        height += 1
        if val <= node.val:
            if node.left:
                self.insertNode(node.left,val,height)
            else:
                node.left = Node(val,node)
                if height > self.height:
                    self.height = height
        if val > node.val:
            if node.right:
                self.insertNode(node.right,val,height)
            else:
                node.right = Node(val,node)
                if height > self.height:
                    self.height = height

    def find(self,val):
        return self.find_node(self.root,val)
        
    def find_node(self,node,val):
       if node is None:
           return None
       elif val == node.val:
           return node
       elif val < node.val:
           return self.find_node(node.left,val)
       else:
           return self.find_node(node.right,val)
                
    def minimum(self,node=None):
        if not node:
            node = self.root
        if node.left:
            return self.minimum(node.left)
        else:
            return node

    def maximum(self,node=None):
        if not node:
            node = self.root
        if node.right:
            return self.maximum(node.right)
        else:
            return node
        
    def sort_tree(self,node=None):
        if not node:
            node = self.root
        if not node.left and not node.right:
            return [node.val]
        elif not node.left and node.right:
            return [node.val] + self.sort_tree(node.right)
        elif node.left and not node.right:
            return self.sort_tree(node.left) +[node.val]
        else:
            return self.sort_tree(node.left) + [node.val] + self.sort_tree(node.right)
        
    def predecessor(self,val,node=None):
        if not node:
            node = self.root
        k = self.find(val)
        if k is None:
            return 'Value not in tree' 
        if k.left:
            return self.maximum(k.left)
        else:
            node = k.parent
            while node is not None:
                if node.val < val:
                    return node
                node = node.parent
            return 'Value is minimum'

    def successor(self,val,node=None):
        if not node:
            node = self.root
        k = self.find(val)
        if k is None:
            return 'Value not in tree'
        if k.right: 
            return self.minimum(k.right)
        else:
            node = k.parent
            while node is not None:
                if node.val > val:
                    return node.val
                node = node.parent
            return 'Value is maximum'

    def select(self,i,node=None):
        if not node:
            node = self.root
        if node.left:
            a = node.left.size
        else:
            a = 0
        if a == (i-1):
            return node.val
        elif a >= i:
            return self.select(i,node.left)
        else:
            return self.select(i-a-1,node.right)
        
    def rank(self,val,node=None,L=0):
        if node is None:
            node = self.root
        if val == node.val:
            if node.left:
                return L + node.left.size + 1
            else:
                return L + 1    
        elif val < node.val:
            return self.rank(val,node.left,L)
        else:
            if node.left:
                L = L + node.left.size + 1
            else:
                L = L + 1
            return self.rank(val,node.right,L)    
                    
    def delete(self,val):
        node = self.find(val)

        if node.left and node.right:
            pred = self.predecessor(node.val)
            if node.parent:
                if node.parent.left:
                    if node.parent.left.val == node.val:
                        node.parent.left = pred
                else:
                    node.parent.right = pred
                    
            if pred.parent:
                if pred.parent.left:
                    if pred.parent.left.val == pred.val:
                        pred.parent.left = pred.left
                else:
                    pred.parent.right = pred.left
            if pred.parent.val == node.val:
                if pred.parent.parent.left == node.val:
                    pred.parent.parent.left = pred.left
                else:
                    pred.parent.parent.right = pred.left
                            
            pred.left = node.left
            pred.right = node.right
   
            node = None

        elif node.left:
            if node.parent.left:
                if node.parent.left.val == node.val:
                    node.parent.left = node.left
            else:
                node.parent.right = node.left

        elif node.right:
            if node.parent.left:
                if node.parent.left.val == node.val:
                    node.parent.left = node.right
            else:
                node.parent.right = node.right

        else:
            if node.parent.left:
                if node.parent.left.val == node.val:
                    node.parent.left = None
            else:
                node.parent.right = None
    
import numpy as np
Tree = BST()
for i in set(np.random.randint(10,200,20)):
    Tree.insert(i)

#import numpy as np
#Tree = BST()
#nodes_to_add = [1,2,4,5,7,8,9,10,12,20,21,22,23,24,25,26,30,33,35,37,40,49,50,52]
#for i in np.random.permutation(len(nodes_to_add)):
#    Tree.insert(nodes_to_add[i])

#Tree = BST()
#for i in nodes_to_add:
#    Tree.insert(i)
    
print 'Minimum value: %s' % Tree.minimum()
print 'Maximum value: %s' % Tree.maximum()
#print 'Precessor of maximum: %s' % Tree.predecessor(Tree.maximum())
#print 'Successor of minimum: %s' % Tree.successor(Tree.minimum())
print 'Ordered values: %s' % Tree.sort_tree()
#print 'Find node value 23: %s' %  Tree.find(23)
print 'Select 4th order statistic: %s' % Tree.select(2)
node = Tree.select(2)
f = Tree.find(node)
print f.left
print f.right
Tree.delete(node)
print Tree.sort_tree()
#print 'Rank of maxmimum value: %s' % Tree.rank(Tree.maximum())
#print 'Height of Tree: %s' % Tree.height
#print 'Number of nodes: %s' % Tree.root.size
