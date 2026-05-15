# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        bfsQ = deque([(root, 1)])
        levelMap = defaultdict(list)
        result = []
        while bfsQ:
            node, level = bfsQ.popleft()
            levelMap[level].append(node.val)
            if node.left:
                bfsQ.append((node.left, level+1))
            if node.right:
                bfsQ.append((node.right, level+1))
        
        for i in levelMap:
            result.append(levelMap[i][-1])
        return result

