def nodefinder(node, head):
    current = head
    while current:
        if current.value == node.value:
            return current
        else:
            current = current.next
    return -1


"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)
            self.length += 1
        elif self.length == 1:
            self.head = ListNode(value, None, self.tail)
            self.length += 1
        else:
            self.head = ListNode(value, None, self.head)
            self.length += 1

    def remove_from_head(self):
        if self.length == 0:
            return 0
        elif self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            self.head = self.head.next
            self.length -= 1

    def add_to_tail(self, value):
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = ListNode(value)
            self.length += 1
        elif self.length == 1:
            temp = self.tail
            new_tail = ListNode(value, self.head, None)
            self.tail = new_tail
            self.head = ListNode(temp.value, None, self.tail)
            self.length += 1
        elif self.length == 2:
            temp = self.tail
            new_tail = ListNode(value, self.tail, None)
            self.tail = new_tail
            self.tail.prev = ListNode(temp.value, self.head, self.tail)
            self.head.next = ListNode(temp.value, self.head, self.tail)
            self.length += 1
        else:
            new_tail = ListNode(value, self.tail, None)
            old_tail = ListNode(self.tail.value, self.tail.prev, new_tail)
            self.tail = new_tail
            self.tail.prev = old_tail
            self.head.next.next.next = old_tail
            self.length += 1

    def remove_from_tail(self):
        if self.length == 0:
            return 0
        elif self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            self.tail = self.tail.prev
            self.length -= 1

    def move_to_front(self, node):
        if self.length == 2:
            temp = self.head
            self.head = ListNode(self.tail.value, None, self.head)
            self.tail = ListNode(temp.value, self.head, None)
        elif self.head.value == node:
            print(f'You cant move the current head forward')
        elif self.head.next == node:
            curr_node = self.head.next
            head_node = self.head
            self.head = ListNode(curr_node.value, None, head_node)
            self.head.next = ListNode(
                head_node.value, self.head, curr_node.next)
        else:
            nodefinderresult = nodefinder(node, self.head)
            if nodefinderresult == -1:
                return print(f'No node found with the value of {node.value}')
            else:
                temp = nodefinderresult.prev
                curr_node = nodefinderresult
                # switch the nodefinderresult
                nodefinderresult = ListNode(temp.value, temp.prev, temp)
                # backwards
                # switch the nodeffinder result next to the front of the node finder result
                nodefinderresult.next = ListNode(
                    curr_node.value, nodefinderresult, curr_node.next)

    def move_to_end(self, node):
        nodefinderresult = nodefinder(node, self.head)
        if self.length == 2:
            temp = self.head
            self.head = ListNode(self.tail.value, None, self.head)
            self.tail = ListNode(temp.value, self.head, None)
        elif self.tail.prev.value == nodefinderresult.value:
            temp = self.tail.prev
            self.tail.prev = ListNode(
                self.tail.value, self.tail.prev, self.tail.next)
            self.tail = ListNode(temp.value, self.tail.prev, None)
        elif self.tail.value == nodefinderresult.value:
            print('Cannot move tail back')
        else:
            curr_node = nodefinderresult
            next_node = nodefinderresult.next
            # Move the previous node next up
            nodefinderresult = ListNode(
                next_node.value, curr_node.prev, curr_node.next)
            nodefinderresult.next = ListNode(
                curr_node.value, next_node.prev, next_node.next)

    def delete(self, node):
        nodefinderresult = nodefinder(node, self.head)
        if nodefinderresult == -1:
            print('No node found on input {node}')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif nodefinderresult.value == self.head.value:
            if self.length == 2:
                self.head = ListNode(self.tail.value, None, self.tail)
                self.tail = ListNode(self.tail.value, self.head, None)
                self.length -= 1
            else:
                self.head = self.head.next
                self.length -= 1
        elif nodefinderresult.value == self.tail.value:
            new_tail = ListNode(self.tail.prev.value,
                                self.tail.prev.prev, None)
            self.tail = new_tail
            self.length -= 1
        else:
            prev_node = nodefinderresult.prev
            next_node = nodefinderresult.next
            nodefinderresult.prev.next = next_node
            nodefinderresult.next.prev = prev_node
            self.length -= 1

    def get_max(self):
        current = self.head
        max_val = 0
        print(self.tail.value, 'taill')
        while current:
            if max_val < current.value:
                max_val = current.value
            current = current.next
        return max_val
