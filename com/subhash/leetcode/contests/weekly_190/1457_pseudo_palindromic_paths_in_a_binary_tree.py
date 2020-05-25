# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0
        self.values = set()

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.pre_order(root)
        return self.count

    def pre_order(self, node: TreeNode):
        added = False
        removed = False
        if node.val in self.values:
            self.values.remove(node.val)
            removed = True
        else:
            self.values.add(node.val)
            added = True

        if node.right is None and node.left is None:
            # leaf node, check set size <= 1
            if len(self.values) <= 1:
                self.count += 1
        else:
            # keep traversing
            if node.left is not None:
                self.pre_order(node.left)

            if node.right is not None:
                self.pre_order(node.right)

        if removed:
            self.values.add(node.val)
        if added:
            self.values.remove(node.val)


if __name__ == "__main__":
    root = TreeNode(1, None, None)
    count = Solution().pseudoPalindromicPaths(root)
    print(count)