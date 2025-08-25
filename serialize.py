# TimeComplexity:O(n)
# SpaceCompelxity:O(1) considering space is given to store nodes else O(n)
# Appraoch:
# You can use standard BFS and use 2m+1 and 2m+2 while deserizling
# DFS approach is little bit tricky , this can be achived by moving idx but idx should be global which  can achiec by idx[0]


######################
# Using BFS
######################


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #use dfs 
        q=deque([])
        q.append(root)
        encode=[]
        while(len(q)):
            l=len(q)
            for _ in range(l):
                node=q.popleft()
                if node:
                    encode.append(str(node.val))
                else:
                    encode.append("null")
                if node:
                    q.append(node.left)
                    q.append(node.right)
        # print(encode)
        return ",".join(encode) #returns string with , seprated
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # [1,2,3,null,null,4,5]
        #  0  1 2 3.    4  5. 6
        #use 2m+1,2m+2 if goes out of bounds use null
        data =data.split(",")
        l=len(data)
        if l==1:return None
        root= TreeNode(data[0])
        data[0]=root
        for i in range(l):
            node= data[i]
            if node==None:continue
            left,right= 2*i+1, 2*i+2
            if left<l:
                node.left=TreeNode(data[left])
                data[left]=node.left
            if right<l:
                node.right=TreeNode(data[right])
                data[right]=node.right
        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


##########################
#Using recursion
##########################


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root,encode):
            if not root:
                encode.append("null")
                return 
            encode.append(str(root.val))
            helper(root.left,encode)
            helper(root.right,encode)
        encode=[]
        helper(root,encode)
        
        return ",".join(encode)
        # print(encode)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # [1,2,3,null,null,4,5]
        #  0  1 2 3.    4  5. 6
        #use 2m+1,2m+2 if goes out of bounds use null
        data = data.split(",")
        # l=len(data)
        # print(l)
        idx=[0]
        def helper():
            #base
            # print(idx)
            if  data[idx[0]]=="null":
                idx[0]+=1
                return None

            #logic
            
            root= TreeNode(data[idx[0]])
            idx[0]+=1
            root.left=helper()
            root.right=helper()
            return root
        
        return helper()
            

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
