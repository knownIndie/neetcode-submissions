# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        cur=head
        sp=cur
        fp=cur
        while fp!=None and fp.next!=None and fp.next.next!=None:
            if sp == fp.next.next:
                return True
            sp=sp.next
            fp=fp.next.next
        return False