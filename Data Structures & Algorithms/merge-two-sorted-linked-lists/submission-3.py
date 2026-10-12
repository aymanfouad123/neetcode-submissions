# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        initial idea: two pointers? 
        where for every higher value we just reference the lower value list

        eventhough we use a dummy list space complexity is considered O(1)
        time O(n+m)
        """
        dummy = ListNode()
        mergedList = dummy    

        while list1 and list2:
            if list1.val < list2.val:
                mergedList.next = list1     # reference the node instead of node.val
                list1 = list1.next
            else:
                mergedList.next = list2
                list2 = list2.next
            
            # make sure to update the mergedList pointer 
            mergedList = mergedList.next
        
        # now before we return, one of the lists can be shorter
        if list1:   
            # i.e, list1 is still remaining
            mergedList.next = list1
        else: 
            mergedList.next = list2
        
        return dummy.next

        
