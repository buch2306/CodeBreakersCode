class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l1 = [] #initializing two lists
        l2 = [] 
        
        if head==None: # taking care of the edge case
            return True
        
        cur = head # initializing the pointer
        while cur: # iterating through the linked list
            l1.append(cur.val) # appending each value to the list
            cur = cur.next
          
        # reversing the linked list
        cur = head
        prev=None
        while cur:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next
        
        #iterating through the reversed list
        while prev:
            l2.append(prev.val) # appending the values to the second list
            prev  = prev.next
        
        return l1==l2 #returning the boolean result