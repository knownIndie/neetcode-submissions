# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(None)
        tmp=dummy
        lc=list1
        rc=list2
        while lc and rc:
            if lc.val<=rc.val:
                tmp.next=lc
                lc=lc.next
                tmp=tmp.next
            else:
                tmp.next=rc
                rc=rc.next
                tmp=tmp.next
        if lc==None:
                tmp.next = rc
        else :
            tmp.next= lc
            
        return dummy.next