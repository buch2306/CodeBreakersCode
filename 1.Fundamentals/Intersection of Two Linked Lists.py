class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        l = set() # initializing a set that would store the addresses of the first list's elements
        cur = headA # initializing the pointer for the first linked list
        cur2 = headB # initializing the pointer for the second linked list
        l.add(cur) # adding the first element of the list
       
        
        while cur: # iterating through all the elements of the list
            cur = cur.next
            l.add(cur) # storing the address of each element
        
        if cur2 in l:  # checking if the first element of list 2 is in the set
            return cur2 # returning the address of intersection
             
        while cur2: # iterating through all the elements of the second list
            cur2 = cur2.next
            if cur2 in l: # checking if the element of list 2 is in the set
                return cur2  # returning the address of intersection
        
        return None # returns None if there is no intersection