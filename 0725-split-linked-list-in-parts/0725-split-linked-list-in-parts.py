# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        ans=[]
        length = 0
        while current:
            length+=1
            current=current.next
        width = length//k
        reminder=length%k
        current=head
        for i in range(k):
            part_head =current
            part_size = width +(1 if i<reminder else 0 )

            for _ in range(part_size-1):
                if current:
                    current=current.next
            
            if current:
                next_part=current.next
                current.next=None
                current=next_part
            ans.append(part_head)
        return ans

            
