class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int,dist=0) -> List[int]:
        if not k:
            return [target.val]
        graph=defaultdict(list)
        q=[root]
        while q:
            curr=q.pop(0)
            if curr.left:
                graph[curr.val].append(curr.left.val)
                graph[curr.left.val].append(curr.val)
                q.append(curr.left)
            if curr.right:
                graph[curr.val].append(curr.right.val)
                graph[curr.right.val].append(curr.val)
                q.append(curr.right)
        res=[]
        visited=set([target.val])
        q2=[(target.val,0)]
        while q2:
            node,dist=q2.pop(0)
            if dist==k:
                res.append(node)
            for adj_node in graph[node]:
                if adj_node not in visited:
                    visited.add(adj_node)
                    q2.append((adj_node,dist+1))
        return res