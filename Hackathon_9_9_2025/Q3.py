class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter node values: ").split()))

head = None
tail = None
for val in values:
    new_node = SinglyLinkedListNode(val)
    if head is None:   
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

print("Linked List elements:")
printLinkedList(head)
