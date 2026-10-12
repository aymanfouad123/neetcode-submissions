# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        iterative approach - reversing one link at a time
        done using tmp variable 
        sort of a two pointer like visual logic
        """

        curr = head     # node we're about to reverse
        prev = None     # curr will point to prev after reversal

        while curr: 
            tmp = curr.next     # preserving next org node 
            curr.next = prev    # current val should point to prev
            prev = curr         
            curr = tmp          # moving to the next node 
        
        # in the end curr becomes null, and
        # prev points to the new head 
        return prev



            
        