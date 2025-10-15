# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS_preorder(self,root,level,res):
        if not root:
            return
        if len(res)< level:
            res.append(root.val)
        self.DFS_preorder(root.right,level+1,res)
        self.DFS_preorder(root.left,level+1,res)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # type: ignore

        res=[]
        self.DFS_preorder(root,1,res)
        return res
        