import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(val=None)
        result_head = result
        list1 = list1 if list1 else ListNode(val=math.inf)
        list2 = list2 if list2 else ListNode(val=math.inf)
        while list1.val != math.inf or list2.val != math.inf:
            if list1.val <= list2.val:
                result.val = list1.val
                list1 = list1.next
                if list1 is None:
                    list1 = ListNode(val=math.inf)
            else:
                result.val = list2.val
                list2 = list2.next
                if list2 is None:
                    list2 = ListNode(val=math.inf)
            if list1.val != math.inf or list2.val != math.inf:
                result.next = ListNode()
                result = result.next
        if result_head.val is None:
            result_head = None
        return result_head


def make_linked_list(list1):
    if not list1:
        node1 = None
        node1_head = None
    else:
        node1 = ListNode(val=list1[0])
        node1_head = node1
    for i in list1[1:]:
        node1.next = ListNode(val=i)
        node1 = node1.next
    return node1_head


def testcase(list1, list2, expected_result):
    list1 = make_linked_list(list1)
    list2 = make_linked_list(list2)
    s = Solution()
    result = s.mergeTwoLists(list1, list2)
    result_list = []
    while result is not None and result.val is not None:
        result_list.append(result.val)
        result = result.next
    assert result_list == expected_result


def test():
    testcase([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    testcase([], [], [])
    testcase([], [0], [0])
    testcase([1, 1, 1, 10], [2, 2, 2, 5, 5], [1, 1, 1, 2, 2, 2, 5, 5, 10])
