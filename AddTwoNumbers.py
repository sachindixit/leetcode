# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode:
    def __init__(self):
        self.start_node = None

    def add_node (self, val=0):

        new_node = Node(val)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.next = new_node;

    def print_list(self):

        if self.start_node is None:
            print ('list is empty')
            return
        n = self.start_node
        while n.next is not None:
            print(n.val)
            n = n.next
        if n.val:
            print(n.val)


class Solution:

    def addTwoNumbers(self, l1, l2):

        node1 = l1
        node2 = l2

        l3 = ListNode()
        total = node1.val+node2.val

        carry = 0
        if total > 9:
            carry = 1
            total = total%10
        l3.add_node(total)

        while node1.next is not None or node2.next is not None:
            if node1.next is not None:
                node1 = node1.next
                val1 = node1.val
            else:
                val1 = 0
                
            if node2.next is not None:
                node2 = node2.next
                val2 = node2.val
            else:
                val2 = 0

            total = val1 + val2 + carry
            if total > 9:
                carry = 1
                total = total % 10
            else:
                carry = 0
            l3.add_node(total)


        if carry == 1:
            l3.add_node(carry)

        return l3.start_node




if __name__ == "__main__":


    l1 = ListNode()
    l1.add_node(9)
    l1.add_node(4)
    l1.add_node(3)
    l1.print_list()

    print('=================')
    l2 = ListNode()
    l2.add_node(5)
    l2.add_node(6)
    l2.add_node(4)
    l2.print_list()
    print('=================')

    solution = Solution()
    print('calling solution.addTwoNumbers')
    sum_of_two_list = atn.addTwoNumbers(l1.start_node,l2.start_node)

    print('print sum_of_two_list')
    sum_of_two_list.print_list()

