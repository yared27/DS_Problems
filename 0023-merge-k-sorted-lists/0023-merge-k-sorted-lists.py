class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for ll in lists:
            temp = ll
            while temp:
                heapq.heappush(minheap, temp.val)
                temp = temp.next
        dummy = ListNode()
        temp = dummy
        while minheap:
            temp.next = ListNode(heapq.heappop(minheap))
            temp = temp.next
        return dummy.next

