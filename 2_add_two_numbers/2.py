class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        lp = l3
        carry_sign = 0
        while l1 is not None:
            if l2 is not None:
                sum_val = l1.val + l2.val + carry_sign
                carry_sign %= 1
                if sum_val >= 10: 
                    carry_sign = 1
                    sum_val %= 10
                lp.next = ListNode(sum_val)
                lp, l1, l2 = lp.next, l1.next, l2.next
            else:   
                lp.next = ListNode(l1.val + carry_sign)
                carry_sign %= 1
                lp, l1 = lp.next, l1.next
        while l2 is not None:
            lp.next = ListNode(l2.val + carry_sign)
            carry_sign %= 1
            lp, l2 = lp.next, l2.next
        return l3.next