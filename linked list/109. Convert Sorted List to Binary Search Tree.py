# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]: # type: ignore
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)  # type: ignore

        slow,fast,slow_prev=head,head,None
        while fast and fast.next:
            slow_prev=slow
            slow=slow.next
            fast=fast.next.next
        node=TreeNode(slow.val) # type: ignore
      
        slow_prev.next=None
        node.left=self.sortedListToBST(head)
        node.right=self.sortedListToBST(slow.next)
        return node



        