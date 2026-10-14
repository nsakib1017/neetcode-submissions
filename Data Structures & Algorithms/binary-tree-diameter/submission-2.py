class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth = {}
        diameter = 0
        stack = [(root, False)]

        while stack:
            node, expanded = stack.pop()
            if not node:
                continue
            if expanded:
                left, right = depth.get(node.left, 0), depth.get(node.right, 0)
                diameter = max(diameter, left + right)
                depth[node] = 1 + max(left, right)
            else:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
        return diameter