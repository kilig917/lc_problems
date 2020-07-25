# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
	carry = 0
    last_carry = 0
    current_l1 = l1
    current_l2 = l2
    head = ListNode()
    current = head
    while current_l1 != None or current_l2 != None or carry == 1:
        current_val = carry
        carry = 0
        if current_l1 != None:
            current_val += current_l1.val
            current_l1 = current_l1.next
        if current_l2 != None:
            current_val += current_l2.val
            current_l2 = current_l2.next
        if current_val >= 10:
            carry = 1
            current_val -= 10
        current.val = current_val
        if current_l1 != None or current_l2 != None or carry == 1:
            current.next = ListNode()
            current = current.next
    return head

# # notes
# # - 1
# head = None
# current = head
# # 就算改变current， head依旧等于None

# # - 2
# head = ListNode() # a
# current = head
# current = current.next # b
# current = ListNode()
# # b并没有连接在a之后

# # - 3
# head = ListNode() # a
# current = head
# current.next = ListNode()
# current = current.next # b
# # b连接在a之后