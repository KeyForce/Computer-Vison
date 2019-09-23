#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (57.67%)
# Likes:    252
# Dislikes: 0
# Total Accepted:    26.5K
# Total Submissions: 46K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 
# 
# 示例 2:
# 
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 
# 
# 
# 
# 说明:
# 
# 
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
# 
# 
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(root):
            if not root:
                return False
            
            left = recurse_tree(root.left)
            right = recurse_tree(root.right)
            
            mid = root == p or root == q
            
            if mid + left + right >= 2:
                self.ans = root
            
            return mid or left or right
        
        recurse_tree(root)
        return self.ans

    # 前序遍历 通过list初始化树
    def ListCreatTree(self, list_tree: 'list', i=0):
        if list_tree[i] == None:
            return None

        root = TreeNode(list_tree[i])
        root.left = self.ListCreatTree(list_tree,2*i+1)
        root.right = self.ListCreatTree(list_tree,2*i+1)
        return root


if __name__ == "__main__":
    null = None
    root = [3,5,1,6,2,0,8,null,null,7,4]
    a = Solution()
    b = a.ListCreatTree(root)
    print(b.left.left.val)

