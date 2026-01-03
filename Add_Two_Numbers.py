class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
        carry = 0

        res = ListNode()
        dummy = ListNode(0, res)

        currl1 = l1
        currl2 = l2

        while currl1 or currl2:
            if currl1 and currl2:
                value = currl1.val + currl2.val + carry
                currl1 = currl1.next
                currl2 = currl2.next
            elif currl1:
                value = currl1.val + carry
                currl1 = currl1.next
            else:
                value = currl2.val + carry
                currl2 = currl2.next

            carry = 0

            if value >= 10:
                carry = 1
                value = value % 10

            res.next = ListNode(value)
            res = res.next

        if carry == 1:
            res.next = ListNode(1)

        return dummy.next.next