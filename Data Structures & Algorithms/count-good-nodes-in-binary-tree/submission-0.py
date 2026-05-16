# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxSofar = float("-inf")
        dfsStack = [(root, maxSofar)]
        countGoodNodes = 0
        
        while dfsStack:
            node,maxSofar = dfsStack.pop()
            if node:
                if node.val >= maxSofar:
                    countGoodNodes+=1
                    maxSofar = max(maxSofar, node.val)
                if node.left:
                    dfsStack.append((node.left, maxSofar))
                if node.right:
                    dfsStack.append((node.right, maxSofar))
        return countGoodNodes

                    
            
