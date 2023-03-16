from queue import Queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        q=Queue()
        q.put(node)
        visited={node.val:Node(node.val,[])}
        while q.empty()==False:
            curr=q.get()
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val]=Node(neighbor.val,[])
                    q.put(neighbor)
                visited[curr.val].neighbors.append(visited[neighbor.val])
        return visited[node.val]