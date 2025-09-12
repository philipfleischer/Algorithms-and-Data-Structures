from Datastructures.linked_list import LinkedList
from typing import List, TypeVar

T = TypeVar("T")

#TODO: Change it to LinkedList?
def merge_sort(link_list: List[T]) -> List[T]:
    """Sorts a linked list in ascending order.
    - Recursively divide the linked list into sublists containing a single node.
    - Repeatedly merge the sublists to produce sorted sublists until one remains.
    
    Returns a sorted linked list. 
    
    Runs in O(k*n*log(n)) time. (Because of bad splitting we get k)"""

    if link_list.size_ll() == 1:
        return link_list
    elif link_list.head is None:
        return link_list

    left_half, right_half = split(link_list)
    left_arr = merge_sort(left_half)
    right_arr = merge_sort(right_half)

    return merge(left_arr, right_arr)

def split(link_list: List[T]) -> List[T]:
    """Divide the unsorted list at midpoint into sublists.
    Takes O(k*log(n)) time. """

    if link_list == None or link_list.head == None:
        left_half = link_list
        right_half = None

        return left_half, right_half
    else:
        size = link_list.size_ll()
        mid = size // 2

        mid_node = link_list.node_at_index(mid-1)

        left_half = link_list
        right_half = LinkedList()
        #right_half = linked_listLinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left_arr: List[T], right_arr: List[T]) -> List[T]:
    """Merges two linked lists, sorting by data in nodes.
    Returns a new, merged list. 
    Runs in O(n) time. """

    #Create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()
    #merged = linked_list.LinkedList()

    #Add a fake head that is discarded later
    merged.add_ll(0)

    #Set current to the head of the linked list
    current = merged.head

    #Obtain head nodes for left and right linked lists
    left_head = left_arr.head
    right_head = right_arr.head

    #Iterate over left and right until we reach the tail node
    # of either
    while left_head or right_head:
        # If the head node of left is None, we are past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
        # If the head node of right is None, we are past the tail.
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater thatn right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged

link_list = LinkedList()
#link_list = linked_list.LinkedList()
link_list.add_ll(10)
link_list.add_ll(2)
link_list.add_ll(44)
link_list.add_ll(15)
link_list.add_ll(200)

print(link_list)
sorted_linked_list = merge_sort(link_list)
print(sorted_linked_list)


