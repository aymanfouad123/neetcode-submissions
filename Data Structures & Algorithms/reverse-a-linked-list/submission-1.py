# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        recursive approach - less optimal than iterative
        
        logic: recursively call function on head.next to reverse rest of the list 

        [1,2,3,4]
        head = 1
        newhead = 1 
        head.next = 2 
            2 -
            newhead = 2
            head.next = 3
            3 - 
                newhead = 3 
                head.next = 4
                4 - 
                    newhead = 4 -- need to return this 
                        now head.next is None 
                        so if statement doesnt trigger
                    head.next = None 
                    return newHead -> return 4
                newhead = 4
                head here is 3 
                so head.next = 4; 4.next = None
                so head.next.next = head  
                overwriting None to become 3 
                means 4.next becomes 3 !!
                    hence the reversal! 
                exit loop
                3.next = None 
                    i.e, so far 4.next -> 3 and 3.next -> None
                return newHead = 4
            here head = 2
            newhead becomes 4 with the return 
            2.next = 3; 3.next => was supposed to be None 
            but we said 3.next = 2 
                where so far 
                    4.next -> 3 and 3.next -> 2
                    so we can see that list is being reversed from
                    [2,3,4]
                    to [4,3,2]
            2.next = None 
            return newhead = 4
        newhead = 4 with the return 
        head here was 1
        1.next=2; 2.next where we did None
        2.next = 1
        1.next = None 
        
        HENCE:
        newHead = 4 from all the loopbacks
        
        and by the end 
        4.next -> 3; 3.next -> 2; 2.next -> 1; 1.next->None 

        recursive solution was not intuitive; 
        initially looks like a typical recursion where initial
        return comes off as some basecase but the 
        recursive nature here isnt the standard approach; 
        lost brain cells
        """
        if not head:    # this is just a check for []
            return None

        newHead = head
        if head.next:          
            newHead = self.reverseList(head.next)
            head.next.next = head  
        head.next = None 

        return newHead
