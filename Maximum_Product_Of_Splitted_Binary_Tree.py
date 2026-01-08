def maxProduct(self, root: Optional[TreeNode]) -> int:
    sums = []

    def findSums(root: Optional[TreeNode]):
        if root is None:
            return 0

        currSum = root.val + findSums(root.left) + findSums(root.right)
        sums.append(currSum)

        return currSum

    total_sum = findSums(root)
    res = float('-inf')
    for currSum in sums:
        res = max(res, currSum * (total_sum - currSum))

    return res % 1000000007