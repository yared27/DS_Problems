class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
        return dummy.next

# Helper function to create a linked list from a list of numbers
def create_linked_list(numbers):
    dummy = ListNode(0)
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

# Accepting input from user
def get_input():
    nums = input("Enter digits in reverse order separated by space (e.g., 2 4 3): ")
    return list(map(int, nums.strip().split()))

if __name__ == "__main__":
    print("Enter first number:")
    l1_input = get_input()
    print("Enter second number:")
    l2_input = get_input()

    l1 = create_linked_list(l1_input)
    l2 = create_linked_list(l2_input)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Resultant sum in reverse order:")
    print_linked_list(result)
