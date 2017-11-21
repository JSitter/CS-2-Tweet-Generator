#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        end = False
        length = 0
        current_position = None

        #check for empty linked list
        if self.head is None:
            return 0

        current_position = self.head
        #count the head
        length += 1
        while not end:
            #See if we hit the end
            if current_position.next is not None:
                #move one down the list and count it
                current_position = current_position.next
                length += 1
            else:
                end = True

        return length

        

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
         O(n) run time under most conditions due to length"""
        
        if self.length() == 0:
            self.head = Node(item)
            self.tail = self.head
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions? 
        O(n) run time under most conditions due to length method"""
        if self.length() == 0:
            self.head = Node(item)
            self.tail = self.head
        else:
            next_item = self.head
            self.head = Node(item)
            self.head.next = next_item

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?
        Best Case runtime is O(1) if the item is the first one in the list
        Worst Case runtime is O(n) if the item is the last one in the list"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        
        if self.head is None:
            return None

        current_position = self.head
        
        while current_position is not None:
            if quality(current_position.data):
                print(current_position.data)
                return current_position.data
            current_position = current_position.next

        return None
            

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.head is None:
            raise ValueError("Item not found: {}".format(item))
        
        previous_item = None
        current_item = self.head
        found = False

        #Iterate over entire list to find matching item
        while current_item is not None and not found:
            #If current_item matches then determine what to do
            if current_item.data == item:
                
                #Check if current item is at the head
                if current_item == self.head:
                    #If only one item in list remove item
                    if current_item.next is None:
                        self.head = None
                        self.tail = None
                        found = True
                    else:
                        self.head = current_item.next
                        found = True
                
                #Check if list item is at Tail
                elif current_item == self.tail:
                    previous_item.next = None
                    self.tail = previous_item
                    found = True
                
                #Else remove from middle
                else:
                    previous_item.next = current_item.next
                    found = True

            #else iterate to next item in list
            previous_item = current_item
            current_item = current_item.next
        if not found:
            #List iteration finished without finding match
            raise ValueError("Item not found: {}".format(item))


    def printList(self):
        llist = ""
        current_position = self.head
        while not current_position:
            llist += current_position.data + "->"
            current_position = current_position.next

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
