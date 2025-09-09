class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")

def reverse(head):
    prev = None
    current = head
    
    while current is not None:
        nxt = current.next   
        current.next = prev  
        prev = current       
        current = nxt        
    
    return prev  


head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)

print("Original List:")
printLinkedList(head)


head = reverse(head)

print("Reversed List:")
printLinkedList(head)
