# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        idea: pointer offset tracking; O(1) space
        """
        slow, fast = head, head

        while fast and fast.next:
            '''
            we can just check for fast 
            since either fast will finish early where next=null 
            or itll catchup to slow first, if a cycle exists
            '''
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True     # cycle exists
        
        return False

