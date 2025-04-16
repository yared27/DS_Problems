class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        return None

def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# ---- User input ----
a = list(map(int, input("Enter List A (space-separated): ").split()))
b = list(map(int, input("Enter List B (space-separated): ").split()))

headA = create_list(a)
headB = create_list(b)

# ---- Find intersection ----
result = Solution().getIntersectionNode(headA, headB)
print("Intersection at:", result.val if result else "No intersection")
