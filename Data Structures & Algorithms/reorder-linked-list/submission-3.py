# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        idea: 
        sort of a merged application of prev qs
        1. use pointers to find midpoint 
        2. we breakup the list in two parts 
        3. reverse the second half 
        4. and, proceed to merge alternatively

        we can also brute force using hashmap and storing indices
        which will be O(n) space
        """

        # 1. find midpoint 
        slow, fast = head, head.next   
        # make sure fast is head.next and not head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # when done slow will be the midpoint for the second half 
        secondList = slow.next
        slow.next = None    # breakpoint   

        # 2. reversing second half 
        prev = None
        while secondList:
            temp = secondList.next      # org next value 
            secondList.next = prev
            prev = secondList
            secondList = temp           # moving to swap next val
        
        # 3. merging two halfs 
        firstList = head
        secondList = prev   # prev will be the head/last element
        while secondList:   # since second half can be smaller 
            temp1 = firstList.next
            temp2 = secondList.next
            firstList.next = secondList
            secondList.next = temp1     
            # now shifting the pointers
            firstList = temp1
            secondList = temp2

        # nothing to return so done
        




