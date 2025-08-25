# TimeComplexity:O(n)
# SpaceCompelxity:O(n) 
# Approach: have idx val while pushing into queue left is idx-1 and right is idx+1 either you can sort it or have min and max use that to amke offset


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([])
        if not root:return []
        q.append((root,0))
        vals=[]
        offset=float('inf')
        mx=0
        while(len(q)):
            k=len(q)
            
            for _ in range(k):
                node,col=q.popleft()
                vals.append((col,node.val))
                if node.left:
                    q.append((node.left,col-1))
                    if col-1<0:
                        offset=min(offset,col-1)
                if node.right:
                    mx=max(mx,col+1)
                    q.append((node.right,col+1))
        if offset!=float("inf"):
            offset=-1*offset
        else:
            offset=0
        ans=[[] for _ in range(mx+offset+1)]
        # print(vals)
        for idx,val in vals:
           
            ans[idx+offset].append(val)
        return ans
      
