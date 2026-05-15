# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        bfsQ = deque([(root, 1)])
        levelMap = defaultdict(list)

        while bfsQ:
            node, level = bfsQ.popleft()
            if node:
                levelMap[level].append(node.val)
                bfsQ.append((node.left, level+1))
                bfsQ.append((node.right, level+1))
        
        for i in levelMap:
            result.append(levelMap[i])
        return result