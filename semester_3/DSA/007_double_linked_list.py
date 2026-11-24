
# Doubly Linked List
# Operations:
# 1. Insert at end
# 2. Insert at start
# 3. Insert at position
# 4. Delete by value
# 5. Display forward
# 6. Display backward


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


# Insert at end
def insert_at_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node

    temp = head

    while temp.next is not None:
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp

    return head


# Insert at start
def insert_at_start(head, value):
    new_node = Node(value)

    if head is not None:
        head.prev = new_node

    new_node.next = head

    return new_node


# Insert at a specific position (1-based indexing)
def insert_at_position(head, value, position):

    if position < 1:
        print("Invalid position!")
        return head

    if position == 1:
        return insert_at_start(head, value)

    new_node = Node(value)

    temp = head
    count = 1

    # Find the node before required position
    while temp is not None and count < position - 1:
        temp = temp.next
        count += 1

    if temp is None:
        print("Position out of range!")
        return head

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next is not None:
        temp.next.prev = new_node

    temp.next = new_node

    return head


# Delete first occurrence of a value
def delete_node(head, value):
    temp = head

    # Find the node
    while temp is not None and temp.data != value:
        temp = temp.next

    if temp is None:
        print("Value not found!")
        return head

    # Update previous node
    if temp.prev is not None:
        temp.prev.next = temp.next
    else:
        head = temp.next

    # Update next node
    if temp.next is not None:
        temp.next.prev = temp.prev

    return head


# Display forward
def display_forward(head):
    temp = head

    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next

    print()


# Display backward
def display_backward(head):
    if head is None:
        print("List is empty!")
        return

    temp = head

    # Move to the last node
    while temp.next is not None:
        temp = temp.next

    # Traverse backward
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.prev

    print()


# Main program
head = None

# Insert nodes at end
n = int(input("Enter number of nodes to insert: "))

for i in range(n):
    val = int(input("Enter value: "))
    head = insert_at_end(head, val)


print("\nDoubly Linked List:")
print("Forward: ", end="")
display_forward(head)

print("Backward: ", end="")
display_backward(head)


# Insert at start
print("\nInsert 100 at start.")
head = insert_at_start(head, 100)

print("Forward: ", end="")
display_forward(head)

print("Backward: ", end="")
display_backward(head)


# Insert at specific position
position = int(input("\nEnter position to insert: "))
value = int(input("Enter value to insert: "))

head = insert_at_position(head, value, position)

print("After inserting at position:")

print("Forward: ", end="")
display_forward(head)

print("Backward: ", end="")
display_backward(head)


# Delete by value
val = int(input("\nEnter value to delete: "))
head = delete_node(head, val)

print("After deletion:")

print("Forward: ", end="")
display_forward(head)

print("Backward: ", end="")
display_backward(head)