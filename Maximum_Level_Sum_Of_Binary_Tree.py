import collections

def maxLevelSum(self, root: Optional[TreeNode]) -> int:
    max_sum = float('-inf')
    max_level = 0
    

    queue = collections.deque()
    queue.append(root)

    level = 0
    while queue:
        level += 1

        currSum = 0
        for i in range(len(queue)):
            node = queue.popleft()
            currSum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if currSum > max_sum:
            max_sum = currSum
            max_level = level

    return max_level