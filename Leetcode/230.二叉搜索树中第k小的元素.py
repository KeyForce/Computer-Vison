#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 二叉搜索树 中序遍历就是一个升序的数组
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 简单方案
        # val = []
        # self.InOrder(root, val)
        # return val[k-1]

        # 生成器 时间复杂度低
        gen = self.InOrderYield(root)
        for _ in range(k):
            k_val = next(gen)
        return k_val        

    # 中序遍历 left>root>right
    def InOrder(self, root, val):
        if root:
            self.InOrder(root.left, val)
            val.append(root.val)
            self.InOrder(root.right, val)
    
    def InOrderYield(self, root):
        if root:
            yield from self.InOrderYield(root.left)
            yield root.val
            yield from self.InOrderYield(root.right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    a = Solution()
    a.kthSmallest(root, k=1)

