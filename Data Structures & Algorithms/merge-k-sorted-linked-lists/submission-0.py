# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # minheap - was initial intuition 
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        mergedList = dummy

        while min_heap:
            # choosing smallest node all list pointers
            _, i, node = heapq.heappop(min_heap)

            # appending the smallest node found
            mergedList.next = node
            
            # advancing the pointer from the list we took from
            node = node.next
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

            # advancing the output pointer
            mergedList = mergedList.next

        return dummy.next