# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        levelMap = defaultdict(list)
        q.append((root, 0))

        while q:
            curr, level = q.popleft()
            if not curr:
                continue
            levelMap[level].append(curr.val)
            q.append((curr.left, level+1))
            q.append((curr.right, level+1))
        
        return list(levelMap.values())
