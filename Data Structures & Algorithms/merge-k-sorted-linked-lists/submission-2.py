# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        initial idea: would be the same as merge 2 linkd?
        we just use the min operator?

        would be a divide and conquer like approach where we can use two merge linkd as helper function 

        theres a few intuitive ways to go about this,
        1. d&c iterative
        2. d&c recursive
        3. minheap
        """
        # d&c recursive 
        if not lists: return None 
        return self.divide(lists, 0, len(lists) - 1) 
    
    def divide(self, lists, left, right):
            if left > right:
                return None
            if left == right:
                return lists[left]

            # divide logic
            mid = (left + right) // 2
            leftList = self.divide(lists, left, mid)
            rightList = self.divide(lists, mid+1, right)

            return self.mergeTwo(leftList, rightList)

    # conquer - same as merge two sorted list q 
    def mergeTwo(self, l1, l2):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2

            return dummy.next
        