class NODE():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)    
        
class LINKED():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    ### PRINT CONTENTS OF LL: O(n)   
    def __str__(self):
        array = []
        node = self.head
        while node != None:
            array.append(str(node.data))
            node = node.next
        return str(array)

    ### APPEND NODE TO LL: O(1)
    def append(self,data):
        self.length += 1
        node = NODE(data)
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.next = node
            self.tail = node
            self.tail.prev = self.head               
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    ### ADD NODE TO BEGINNING OF LL: O(1)
    def addFirst(self,data):
        self.length += 1
        node = NODE(data)
        self.head.prev = node
        node.next = self.head
        self.head = node            
            
    ### REMOVE AND RETURN TAIL: O(1)        
    def pop(self):
        self.length -= 1
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return data

    ### CONVERT LL TO LIST: O(n)
    def tolist(self):
        array = []
        node = self.head
        while node != None:
            array.append(str(node.data))
            node = node.next
        return array

    ### DELETE A NODE: O(n)
    def delete(self,index):
        self.length -= 1
        node = self.head
        ind = 0
        while ind < index:
            node = node.next
            ind += 1
        nodeA = node.prev
        nodeB = node.next
        nodeA.next = nodeB
        nodeB.prev = nodeA

    ### INSERT A NODE: O(n)
    def insert(self,index,data):
        self.length += 1
        node = self.head
        ind = 0
        while ind < index:
            node = node.next
            ind += 1
        new = NODE(data)
        after = node
        before = node.prev
        new.next = after        
        new.prev = before
        before.next = new
        after.prev = new

    ### COPY THE LINKED LIST: O(n)
    def copy(self):
        newH = LINKED()
        node = self.head
        while node != None:
            newH.append(node.data)
            node = node.next
        return newH
        
if __name__ == "__main__":

    L = [4,2,5,6,7,8,9,10]
    H = LINKED()
    for item in L:
        H.append(item)
    print H
    print H.length
    H.pop()
    print H
    print H.length
    Y = H.tolist()
    H.insert(3,100)
    print H
    print H.length


    # Find Loop in Linked List
    # Reverse a Linked List w/ w/o Recursion
    # Find the kth last entry of linked list
    # Queue/Stack Single or Double?
    # Find middle node of linked list
    # Sort a linked list
    # Remove all values equal to x in linked list
    # Convert Binary Tree to DLL - Inorder Traversal
    
