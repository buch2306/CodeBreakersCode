# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# used the two pointer approach
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    
    first = head # initializing the first pointer
    second = head # initializing the second pointer
    count = 1 # initializing the counter
    
    while count<=k:  # counting until k
        second =second.next  # traversing the list until we reach the kth position
        count += 1

    if second is None:  # if k is equal the length of the list, then we remove the first element of the list
        head.value  = head.next.value # swapping the second node's value with the first
        head.next = head.next.next #connecting the first node to the third node
        return

    while second.next: # traversing the remaining list until we reach the end
        second = second.next 
        first = first.next

    first.next = first.next.next # the head reaches the node behind the node to be eliminated, simply connecting this node to the node that comes after the target node  
