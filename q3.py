class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next
            
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head

        while p_curr != None and q_curr != None:

            p_next = p_curr.next
            q_next = q_curr.next
            q_curr.next = p_next 
            p_curr.next = q_curr 
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr



llist1 = LinkedList()
llist2 = LinkedList()

llist1.push(18)
llist1.push(17)
llist1.push(7)
llist1.push(8)

llist2.push(4)
llist2.push(2)
llist2.push(10)
llist2.push(32)
print("First Linked List:")
llist1.printList()

print("\nSecond Linked List:")
llist2.printList()

llist1.merge(p=llist1, q=llist2)

print("\nModified first linked list:")
llist1.printList()

print("\nModified second linked list:")
llist2.printList()